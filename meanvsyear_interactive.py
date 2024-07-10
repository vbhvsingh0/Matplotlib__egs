%matplotlib widget
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm
from matplotlib.widgets import Slider

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

indxs = list(df.index)

#calculating standard deviation  

means = [df.loc[ix,:].mean() for ix in indxs]
means1 = pd.DataFrame({'means':[np.random.normal(32000,200000,3650).mean() for i in range(1000)]})
means2 = pd.DataFrame({'means':[np.random.normal(43000,100000,3650).mean() for i in range(1000)]})
means3 = pd.DataFrame({'means':[np.random.normal(43500,140000,3650).mean() for i in range(1000)]})
means4 = pd.DataFrame({'means':[np.random.normal(48000,70000,3650).mean() for i in range(1000)]})

std1 = means1.std(axis = 0)
std2 = means2.std(axis = 0)
std3 = means3.std(axis = 0)
std4 = means4.std(axis = 0)

stds = [std1[0],std2[0],std3[0],std4[0]]
#df.loc[1992,:].mean()
x = [str(1992),str(1993),str(1994),str(1995)]      # saving stdvs as a list

#This is a monte carlo method to calculate the probability of any y value to be in the current distrubition mean

def probf(cy, c_mean):
    A = pd.DataFrame(c_mean['means'] > cy) 
    pb = (A['means'].value_counts().get(True,0))/1000    # checks if chosen cy is greater than the randomly chosen mean from the data
    return pb

ccy = 42000                                              # check was done cy = 42000, initial cy value
 
p1 = probf(cy = ccy, c_mean = means1)
p2 = probf(cy = ccy, c_mean = means2)
p3 = probf(cy = ccy, c_mean = means3)
p4 = probf(cy = ccy, c_mean = means4)

probs = [p1,p2,p3,p4]                              

#fig = plt.figure(figsize=(9.6,7.2));
#plt.bar(x, means, width = 0.9, yerr=stds,capsize = 16);
fig, ax = plt.subplots(figsize=(9.6,7.2))
bars = ax.bar(x, means, width = 0.9, yerr=stds, capsize=16);
plt.xlabel('Year', fontsize = 16);
plt.ylabel('Means', fontsize = 16);
plt.xticks(fontsize = 13);
plt.yticks(fontsize = 13);
plt.suptitle('Means at different year',fontsize = 16);

# Create a colormap
cmap = cm.get_cmap('coolwarm')

#Purpose: Normalization is essential when you want to map data values to a colormap because colormaps 
#typically expect input values in the range [0, 1]. By normalizing your data, you ensure
#that the entire range of your colormap is utilized appropriately.

norm = mcolors.Normalize(vmin=0, vmax=1) 

# Add colorbar
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, orientation='horizontal', pad=0.1)
#cbar.set_label('Probability', fontsize = 14)

for bar, prob in zip(bars, probs):
    bar.set_color(cmap(norm(prob)))
    
# plotting horizontal line for the widget
hline = plt.axhline(y = ccy,color = 'blue',linestyle = '--');

# Slider setup
ax_slider = plt.axes([0.9, 0.3, 0.01, 0.58], facecolor = 'lightgray')                        # defines size of the slider and color by creating new axis
slider = Slider(ax_slider, 'Y Value', 0, 50000, valinit=ccy, orientation = 'vertical')       # converting axis plotted above to a slider

# Update function
def update(val):
    y_value = slider.val
    hline.set_ydata(y_value)
    p11 = probf(y_value, means1)
    p21 = probf(y_value, means2)
    p31 = probf(y_value, means3)
    p41 = probf(y_value, means4)
    probs = [p11,p21,p31,p41]
    for bar, prob in zip(bars, probs):
        bar.set_color(cmap(norm(prob)))
    fig.canvas.draw_idle()

# Connect the slider to the update function
slider.on_changed(update)

plt.show()