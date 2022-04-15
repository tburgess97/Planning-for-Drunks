'''
Agent (Drunk) class
Contains agents (drunks) attributes and their behaviours

As ran through drunk.py

Version 1

Author: 201466497, University of Leeds

As produced for GEOG5990: Assignment 2
'''


# Packages and modules 

# Import the packages and modules required for this model

# Standard library 
import random


# Agent (Drunk) class 

# Initiate a Drunk class for the agents and define their behaviours as 
# functions

class Drunk():
    
    def __init__(self, environment, house, density):
        '''
        Function to initiate the drunk agent; reads in the environment and sets
        starting y and x coordinates at the centre of the pub, takes in the 
        assignment of an individual house number and records each step to be 
        plotted as a density map.

        Parameters
        ----------
        environment :
            ENVIRONMENT AS THE town.txt FILE AS READ IN FROM 
            Drunksmodel.py AS A 2D LIST.
        house : 
            THE DRUNK'S INDIVIDUAL HOUSE NUMBER AS ASSIGNED IN Drunksmodel.py.
        density : 
            RECORDS EACH STEP OF THE DRUNK ON IT'S ROUTE HOME TO THEN BE USED 
            TO PLOT A DENSITY MAP.

        Returns
        -------
        None.

        '''
        self.environment = environment
        self.y = 148
        self.x = 138
        self.house = house
        self.density = density
        
        
    def move(self):
        '''
        A function to move the drunk by one step in a random direction and 
        apply a fence boundary affect to the drunk

        Returns
        -------
        The new y coordinate.
        The new x coordinate.

        '''
        if random.random() < 0.5:
            self.y = (self.y + 1)
        else:
            self.y = (self.y - 1)
        
        if random.random() < 0.5:
            self.x = (self.x + 1)
        else:
            self.x = (self.x - 1)
            
        # Fence boundary affect to keep the agent within the environment limits
        if self.y < 0:
            self.y = 0
        if self.y > 299:
            self.y = 299
        
        if self.x < 0:
            self.x = 0
        if self.x > 299:
            self.x = 299
            
    
    def add_density(self):
        '''
        A function to record the coordinates of each step that a drunks takes
        on it's route home by adding a value of 1 to each coordinate it takes

        Returns
        -------
        The value of the frequency that a coordinate from the environment has 
        been 'stepped on'.

        '''
        self.density[self.y][self.x] += 1