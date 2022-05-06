'''
Planning for Drunks Model

Version 1

Author: 201466497, University of Leeds

As produced for GEOG5990: Assignment 2

To be run in the command prompt as per the README documentation
'''


# Packages and modules 

# Import the packages and modules required for this model

# Standard library 
import csv
import argparse

# Third party
import matplotlib
import matplotlib.pyplot

# Local application
import Drunksframework

print("Libraries and modules imported")


# Command line run set up

# Argparse used to set up the model to be run from the command prompt 
# Command line argument source code adapted from:
    # https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description = 'Planning for Drunks Model')
args = parser.parse_args()


# Environment 

# Create an environment container
environment = []

# Read in the environment as raster data
f = open('town.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Append the raster data to the environment as a 2D list 
for row in reader: 
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()
# Uncomment to check the raster environment
'''
print(environment)
'''

# Check the environment parameters to inform the axis limits to be plotted
height = len(environment)
width = len(environment[0])
# Uncomment to check the limits of the environment
'''
print("Height =", len(environment), "Width =", len(environment[0]))
'''

# Makes the pub and houses clearer on the display by assigning the pub values
# = -60 vs the initial = 1 as the environment is displayed as a raster
for i in range(len(environment)):
    for j in range(len(environment[i])):
        if environment[i][j] == 1:
            environment[i][j] = -60

# Set the display parameters for the environment and show the environment
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.jet()
matplotlib.pyplot.title("Pub and House Town Plan")
matplotlib.pyplot.imshow(environment)
print("Figure shows the town with the central pub and encircling local houses")
print("Close the figure to continue the model")
matplotlib.pyplot.show()


# Denisty map 

# Initialise a blank initial density map using the same limits as the town plan

# Create a density map container 
density = []

# Read in the town plan txt file to be used as a template for the denisty map
# so that the limits of the environment are used
f1 = open('town.txt', newline='')
reader = csv.reader(f1, quoting=csv.QUOTE_NONNUMERIC)

# Append 0 values for each 'coordinate' of the density map to create a blank
# initial density map
for row in reader: 
    rowlist = []
    for value in row:
        value = 0
        rowlist.append(value)
    density.append(rowlist)
f1.close()
# Uncomment to check a blank density map has been appended 
'''
print(density)
'''


# Drunks 

# Creates and models individual drunks walking to their individual homes after
# leaving the same centralised pub and tracks each drunks route home

# Initialise the drunks 

# Create a drunks container and set the number of drunks to 25 and the amount 
# of drunks at home to 0
drunks = []
num_of_drunks = 25
drunks_home = 0

# Creates the drunks as per the Drunk class and appends their house numbers to 
# them
for i in range(num_of_drunks):
    drunk_ID = (i + 1)
    house = (drunk_ID) * 10
    drunks.append(Drunksframework.Drunk(environment, house, density))
    # Uncomment to check that each drunk can identify their own house 
    '''
    print("I am drunk no.", drunk_ID, "and live at house no.", house)
    '''
    # Uncomment to check that each drunk starts in the pub
    '''
    if drunks[i].y == 148 and drunks[i].x == 138:
        print("and I am in the pub")
    '''
print("Pub closed! Time to go home!")    
    
# Models each drunks route from the centralised pub to their individual home
# whilst tracking their route until all drunks are home
for i in range(num_of_drunks):
    while (environment[drunks[i].y][drunks[i].x] != drunks[i].house):
        drunks[i].move()
        drunks[i].add_density()
        # Uncomment to see the model running in real time with each step taken
        # *Not recommended unless checking the model as takes considerable time
        # for each drunk to get home when each step is printed (ca. 5-15mins)*
        '''
        print("1 drunken step")
        print(drunks[i].y, drunks[i].x)
        '''
    if (environment[drunks[i].y][drunks[i].x] == drunks[i].house):
        drunks_home = drunks_home + 1
        print("Drunk safely home")
        print("No. of drunks home =", drunks_home)

# Confirm that all drunks made it to their homes 
if drunks_home == 25:
    print("All drunks safely home!")


# Density Map Output 

# Plots the drunks routes home as a density output txt.file and saves and 
# displays it

# Opens a txt file and writes in the density data modelled as a 2D list
with open('drunk_density_map.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in density:
        csvwriter.writerow(row)

# Displays the density map as a figure 
matplotlib.pyplot.imshow(density)
matplotlib.pyplot.xlim(0, 299)
matplotlib.pyplot.ylim(0, 299)
matplotlib.pyplot.hot()
matplotlib.pyplot.title("Density Map of Drunk's Route Home")
matplotlib.pyplot.colorbar()
print("Figure shows the density map of the drunk's routes home")
print("Density map saved (txt. file) to the local location of the saved model")
print("Close the figure to finish model")
matplotlib.pyplot.show()

# Confirms that the model has been fully run
print("MODEL FINISHED")