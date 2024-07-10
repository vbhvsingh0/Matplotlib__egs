import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from calendar import month_abbr


df = pd.read_csv('assets/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
print(df.head())

df1 = df
df1['Date'] = pd.to_datetime(df1['Date'])
df1 = df1.set_index('Date').sort_index()       # sorting along date

df_new = df
#converting Fahrenheit into celcius
df_new['Data_Value'] = df_new['Data_Value'] .apply(lambda x: x/10)
#filtering out leap year dates
df_new['Date'] = pd.to_datetime(df_new['Date'])
df_new = df_new[~((df_new['Date'].dt.month == 2) & (df_new['Date'].dt.day == 29))]
df_new = df_new.set_index('Date').sort_index()
#extracting rows with maximum (TMAX) and minimum (TMIN) temperatures
df_tmax=df_new[df_new['Element']=='TMAX']['Data_Value']
df_tmin=df_new[df_new['Element']=='TMIN']['Data_Value']

#dropping the leap year Feb 29 values, Already done in above cell
# create a DataFrame group of maximum temperature by date
df_tmax_05to14 = df_tmax.loc['2005-01-01':'2014-12-31']# Separate the data of 2005-2014 for tmax
df_tmax_15 = df_tmax.loc['2015-01-01':'2015-12-31']# Separate the data of 2015 for tmax


# create a DataFrame group of minimum temperatures by date
df_tmin_05to14 = df_tmin.loc['2005-01-01':'2014-12-31']# Separate the data of 2005-2014 for tmin
df_tmin_15 = df_tmin.loc['2015-01-01':'2015-12-31']# Separate the data of 2015 for tmin

# calculate the minimum and maximum values for the day of the year for 2005 through 2014
#Maximum and minimum of temperatures on each day irrespective of the year
df_tmax_05to14 = df_tmax_05to14.reset_index()
df_tmax_05to14['Month_Day'] = df_tmax_05to14['Date'].dt.strftime('%m-%d')
df_tmax_05to14_max_and_min = df_tmax_05to14.groupby('Month_Day').agg([max,min])['Data_Value'].round(1)

df_tmin_05to14 = df_tmin_05to14.reset_index()
df_tmin_05to14['Month_Day'] = df_tmin_05to14['Date'].dt.strftime('%m-%d')
df_tmin_05to14_max_and_min = df_tmin_05to14.groupby('Month_Day').agg([max,min])['Data_Value'].round(1)

# calculate the minimum and maximum values for the years 2015
#Maximum and minimum of temperatures on each day for the year 2015
df_tmax_15 = df_tmax_15.reset_index()
df_tmax_15['Month_Day'] = df_tmax_15['Date'].dt.strftime('%m-%d')
df_tmax_15_max_and_min = df_tmax_15.groupby('Month_Day').agg([max,min])['Data_Value'].round(1)
df_tmax_15_max_and_min = df_tmax_15_max_and_min.reset_index()

#dates index values
dates_ind = pd.date_range(start='2015-01-01', end='2015-12-31').strftime('%m-%d').tolist()

#out of range max temperatures for year 2014
df_tmax_15_out = pd.DataFrame((np.where(df_tmax_15_max_and_min['max'] > df_tmax_05to14_max_and_min.reset_index()['max'], df_tmax_15_max_and_min['max'] ,np.nan)), index = dates_ind).dropna()

df_tmin_15 = df_tmin_15.reset_index()
df_tmin_15['Month_Day'] = df_tmin_15['Date'].dt.strftime('%m-%d')
df_tmin_15_max_and_min = df_tmin_15.groupby('Month_Day').agg([max,min])['Data_Value'].round(1)
df_tmin_15_max_and_min = df_tmin_15_max_and_min.reset_index()

#out of range min temperatures for year 2014
df_tmin_15_out = pd.DataFrame((np.where(df_tmin_15_max_and_min['min'] < df_tmin_05to14_max_and_min.reset_index()['min'], df_tmin_15_max_and_min['min'] ,np.nan)), index = dates_ind).dropna()

#resetting index for of range 2015 data for scatter plots
df_tmax_15_out = df_tmax_15_out.reset_index()
df_tmin_15_out = df_tmin_15_out.reset_index()


# Set the font size
plt.rcParams['font.size'] = 24

#line plotting the maximum and minimum from 2005 to 2014
plt.figure(figsize=(16,12))
plt.plot(df_tmax_05to14_max_and_min['max'], '-', df_tmin_05to14_max_and_min['min'], '-')

ax = plt.gca()
#Labeling the axes
ax.set_xlabel('Month')
ax.set_ylabel('Temperature (Celcius)')
#Title
ax.set_title("Record Breaking temperatures in 2015")
#scatter plot from the year 2015
plt.scatter(df_tmax_15_out['index'][:], df_tmax_15_out[0][:], s=50, c='red', label='MAX_T(2015)')
plt.scatter(df_tmin_15_out['index'][:], df_tmin_15_out[0][:], s=50, c='red', label='MIN_T(2015)')
#shading the area in between
plt.gca().fill_between(range(len(df_tmax_05to14_max_and_min['max'])), 
                       df_tmax_05to14_max_and_min['max'], df_tmin_05to14_max_and_min['min'], 
                       facecolor='gray', 
                       alpha=0.30)
#Legends
plt.legend(['T$_{MAX}$ (2005-2014)','T$_{MIN}$ (2005-2014)','T$_{record}$ (2015)'],loc=2,prop={'size': 18},frameon=False)

#Changing X-axis tic lebels
months = pd.date_range(start='2024-01-01', end='2024-12-01', freq='MS')
month_names = months.strftime('%b').tolist()   #creates abbreviated month names list
#create positions for each x tick value
days_in_month = np.array([15.5, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
pos = np.cumsum(days_in_month)
#pos = list(sums/2)


plt.xticks(pos,month_names,alpha=0.8)
plt.savefig("assignment_w2.png")
