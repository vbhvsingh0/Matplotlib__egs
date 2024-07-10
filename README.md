# Matplotlib__egs
The codes here are the examples of using Matplotlib

Note: This codes here were a part of the Coursera course, "Applied Plotting, Charting and data representation in Python" offered by University of Michigan.

There are three codes here:

1) Plotting weather pattern

The data for this assignment comes from a subset of The National Centers for Environmental Information (NCEI) Global Historical Climatology Network daily (GHCNd) (GHCN-Daily). The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe - it's a wonderfully large dataset to play with! In particular,  use data from the Ann Arbor Michigan location (my home!). and this is stored in the file: fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv

Each row in this datafile corresponds to a single observation from a weather station, and has the following variables:

    id : station identification code
    date : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
    element : indicator of element type
        TMAX : Maximum temperature (tenths of degrees C)
        TMIN : Minimum temperature (tenths of degrees C)
    value : data value for element (tenths of degrees C)

Following steps were followed in order to plot the data:

    * Read the documentation and familiarize yourself with the dataset, then write a python notebook which plots line graphs of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
    * Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015. (Based on the graph, do you think extreme weather is getting more frequent in 2015?)
    (Leap years were removed)
 
Output: weather_pattern.png


2) Average of mean of some quantity vs years

The code here plots the mean of the quantity (here produced with random number generator but example can be average voting turnover in a country) as bar charts for the years 1992,1993,1994,1995. The standard deviation of the means were also calculated and displayed with error bars on the bar chart.

Here is the twist: Depending upon the y-value chosen from the bar chart (interactively), the color of the bars will change displaying the confidence level of whether the y-value will be involved in the data of each year or not. This confidence level was calculated using Monte Carlo.

Output snipped is saved as meansvsyear_int.png

3) Creating an animation of changing 4 random number distributions with changing sample-size. Animation function was used and the results are provided in hists_animation.gif.


