#!/usr/bin/python

# User ID: considerateGiraffe
# Date Last Edited: 02/09/17
# Challenge Number: 1

# IMPORTANT NOTE: This program was coded in Python 3.

""" Import Statements """
# import the abiliity to divide without throwing errors
from __future__ import division
# import the ability to plot data graphically
import matplotlib.pyplot as mplot

""" Reading In/Splitting Files """
# open and read in the data from the downloaded CSV file
rawData = open("considerateGiraffe_ch1.csv", "r")
rawData = rawData.read()
# Split the file's data at the end of every line
rawData = rawData.split("\n")

# create a set to identify the unique frequencies in the data
uniqueFrequencies = set()

# iterate through the raw data and seperate it after every comma
for index in range(0, len(rawData)):
    # ensure that no empty data lines will get in the way of what we are doing
    if len(rawData[index]) == 0:
        del(rawData[index])
        continue

    rawData[index] = rawData[index].split(",")

    # convert the data into numbers for later usage as such
    rawData[index][0] = float(rawData[index][0])
    rawData[index][1] = float(rawData[index][1])
    rawData[index][2] = float(rawData[index][2])

    # add the frequency values to a set to get only unique values
    addMe = rawData[index][2]
    uniqueFrequencies.add(addMe)

""" Decide Which Frequncy Is Good """
# turn the frequncies set into a list for iteration purposes
uniqueFrequencies = list(set(uniqueFrequencies))

# store both frequencies to the "good frequency" variable; whichever is BAD, comment that assignment out
# goodFrequency = uniqueFrequencies[0] <--- this was the bad frequency
goodFrequency = uniqueFrequencies[1]

""" Scatter Plot Code """
# create new sets for the scatter plot data points
scatter_xaxis = []
scatter_yaxis = []

# add the scatter-plot data from only the good signal to those lists from the new scatter plot sets
for index in range(0, len(rawData)):
    if rawData[index][2] == goodFrequency: # 46.142764 is the frequency that isn't transmitting noice
        scatter_xaxis.append(rawData[index][0])
        scatter_yaxis.append(rawData[index][1])

#turns our two axes lists into one list
sorted_scatter_data = zip(scatter_xaxis, scatter_yaxis)
sorted_scatter_data = sorted(sorted_scatter_data)

#get those newly sorted lists back into two different lists
scatter_xaxis, scatter_yaxis = zip(*sorted_scatter_data)

""" Mean Value Line Plot Code """
# create new sets for the mean value line plot
mean_xaxis = []
mean_yaxis = []

# create some dictionaries to help find the average values for each x-axis value
count = {}
sum = {}

#add the correct values to these new dictionaries
for index in range(0, len(rawData)):
    if rawData[index][2] == goodFrequency:
        milliseconds = rawData[index][0]
        amplitude = rawData[index][1]

        #try-and-catch block to prevent manipulating values that don't exist yet
        try:
            sum[milliseconds] += amplitude
            count[milliseconds] += 1
        except:
            sum[milliseconds] = amplitude
            count[milliseconds] = 1

#turn the sum of each column into an average
for milliseconds,amplitude in count.items():
    sum[milliseconds] /= count[milliseconds]

    #make sure there are no divide-by-zero errors
    if milliseconds == 0:
        continue
    #add the x-axis values and the y-value averages (as a percentage of the x-axis value) to the axis lists to be plotted
    mean_xaxis.append(milliseconds)
    mean_yaxis.append(sum[milliseconds])

#turns our two axes lists into one list
sorted_mean_data = zip(mean_xaxis, mean_yaxis)
sorted_mean_data = sorted(sorted_mean_data)

#get those newly sorted lists back into two different lists
mean_xaxis, mean_yaxis = zip(*sorted_mean_data)

""" Plotting Code """
# set the axes' labels to understandable and helpful values
mplot.xlabel("Transmission Time (ms)")
mplot.ylabel("Amplitude")

# print out the scatter plot and the mean value line plot
mplot.scatter(scatter_xaxis, scatter_yaxis, color="red")
mplot.plot(mean_xaxis, mean_yaxis, lw=5, color="blue")
mplot.show()
