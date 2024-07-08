#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:41:06 2024

@author: Sachin Borade
"""
# Write a python program to draw a line with suitable label in 
import matplotlib.pyplot as plt
X = range(1,50)
y = [value*3 for value in X]
print("Values pf X:")
print(*range(1,50)) # This is how we use *range
'''
    This is equivalent to-
    for i in range(1,50):
        print(i,end=' ')
'''
print("Values of Y (thrice of X):")
print(y)

# Plot the lines and markers to the Axes
plt.plot(X,y)
# Setting the labels to x-axis
plt.xlabel("X-Axis")  
# Setting the labels to y-axis
plt.ylabel("Y-Axis")  
# Setting the title to graph
plt.title("Sample Graph 1") 
# Display the Figure 
plt.show()

##################################################################

# x values are 
X = [1,2,3]
#y values are 
y = [2,4,1]

# Plot the lines and markers to the Axes
plt.plot(X,y)
# Setting the labels to x-axis
plt.xlabel("X-Axis")  
# Setting the labels to y-axis
plt.ylabel("Y-Axis")  
# Setting the title to graph
plt.title("Sample Graph 2") 
# Display the Figure 
plt.show()


##################################################################

# Write a Python Program to plot two or more lines
# on same plot with suitable legends of each line 
import matplotlib.pyplot as plt 

# line 1 point
x1 = [10,20,30]
y1 = [20,30,10]

# line 2 point
x2 = [10,20,30]
y2 = [40,10,30]

# plotting the title 
plt.title("Plotting the two or more lines ")

# plotting the line1 points 
plt.plot(x1,y1,label='line 1')
plt.xlabel('x - axis')
# plotting the line2 points
plt.plot(x2,y2,label='line 2')
plt.ylabel('y - axis')

# Show the legend on the line
plt.legend()

# Display the figure
plt.show()


##################################################################


# Changing the parameters

import matplotlib.pyplot as plt 

# line 1 point
x1 = [10,20,30]
y1 = [20,30,10]

# line 2 point
x2 = [10,20,30]
y2 = [40,10,30]

# plotting the title 
plt.title("Plotting the two or more lines with different color and width ")
# plotting the line1 points 
plt.plot(x1,y1,color='blue',linewidth=3,label='line 1')
plt.xlabel('x - axis')
# plotting the line2 points
plt.plot(x2,y2,color='red',linewidth=5,label='line 2')
plt.ylabel('y - axis')

# Show the legend on the line
plt.legend()

# Display the figure
plt.show()

##################################################################



import matplotlib.pyplot as plt 

# line 1 point
x1 = [10,20,30]
y1 = [20,30,10]

# line 2 point
x2 = [10,20,30]
y2 = [40,10,30]

# plotting the title 
plt.title("Plotting the two or more lines with different linestyle ")
# plotting the line1 points 
plt.plot(x1,y1,color='blue',linewidth=3,label='line 1',linestyle='dotted')
plt.xlabel('x - axis')
# plotting the line2 points
plt.plot(x2,y2,color='red',linewidth=5,label='line 2',linestyle='dashed')
plt.ylabel('y - axis')

# Show the legend on the line
plt.legend()

# Display the figure
plt.show()

##################################################################


"""
Created on Thu Apr 25 08:33:17 2024

@author: Sachin Borade
"""
##################################################################

# Introducing marker in the graph
import matplotlib.pyplot as plt
# X-axis values
x = [1,4,5,6,7]
# Y-axis values
y = [2,6,3,6,3]

#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)
# Set the y-limits of the current axes.
plt.ylim(1,8)
# Set the x-limits of the current axes.
plt.xlim(1,8)

#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')

# Giving the title to my graph 
plt.title('Display Marker')
# Function to show the plot 
plt.show()

##################################################################

# Write a Python programming to display a bar chart of the 
# popularity of programming language
import matplotlib.pyplot as plt
x = ['java','python','PHP','javascript','c++','C#']
popularity = [22.2,17.6,8.8,7.7,6.7,5.2]
x_pos = [i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel('languages')
plt.ylabel('popularity')
plt.title("Popularity of programming language \n" + 
          "Worldwide, OCT 2017 compared to a year ago ")
plt.xticks(x_pos, x)
# Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################################

# Write a python programming to display a horizontal bar chart of 
# the popularity of programming language

import matplotlib.pyplot as plt
x = ['java','python','PHP','javascript','c++','C#']
popularity = [22.2,17.6,8.8,7.7,6.7,5.2]
x_pos = [i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='green')
plt.ylabel('languages')
plt.xlabel('popularity')
plt.title("Popularity of programming language \n" + 
          "Worldwide, OCT 2017 compared to a year ago ")
plt.yticks(x_pos, x)
# Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################################

# Use different color for different bar charts 

import matplotlib.pyplot as plt
x = ['java','python','PHP','javascript','c++','C#']
popularity = [22.2,17.6,8.8,7.7,6.7,5.2]
x_pos = [i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color=['green','red','black','yellow','orange','purple'])
plt.ylabel('languages')
plt.xlabel('popularity')
plt.title("Popularity of programming language \n" + 
          "Worldwide, OCT 2017 compared to a year ago ")
plt.yticks(x_pos, x)
# Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################################

# Use different color for different bar charts 

import matplotlib.pyplot as plt
x = ['java','python','PHP','javascript','c++','C#']
popularity = [22.2,17.6,8.8,7.7,6.7,5.2]
x_pos = [i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['green','red','black','yellow','orange','purple'])
plt.xlabel('languages')
plt.ylabel('popularity')
plt.title("Popularity of programming language \n" + 
          "Worldwide, OCT 2017 compared to a year ago ")
plt.xticks(x_pos, x)
# Turn on the grid 
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##################################################################

import matplotlib.pyplot as plt 
blood_sugar = [113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar, rwidth=0.8) 
# By default the number of bins are set to 10

plt.hist(blood_sugar, rwidth=0.5,bins=4)
# Here we are giving the bins as 4

plt.xlabel("Sugar Level")
plt.ylabel("Number of Patients" )
plt.title("Blood Sugar Chart")
plt.hist(blood_sugar, bins=[80,100,125,150], rwidth=0.95, color='g')

##################################################################

## BOX PLOT 

import matplotlib.pyplot as plt
import numpy as np

#Creating dataset 
np.random.seed(10)
data = np.random.normal(100,20,200)

fig = plt.figure(figsize=(10,7))
# Creating plot
plt.boxplot(data) 
# Show plot
plt.show()

'''
for plotting the BOX PLOT we just need to pass the parameter
'''
##################################################################

import matplotlib.pyplot as plt
import numpy as np

# Creating dataset 
np.random.seed(10)

data_1 = np.random.normal(100,10,200)
data_2 = np.random.normal(90,20,200)
data_3 = np.random.normal(80,30,200)
data_4 = np.random.normal(70,40,200)

data = [data_1,data_2,data_3,data_4]
fig = plt.figure(figsize=(10,7))

# Creating axes instance 
ax = fig.add_axes([0,0,1,1])
# Creating plot 
bp = ax.boxplot(data)
# show plot
plt.show()

##################################################################
