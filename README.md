# Planning for Drunks Model
**[This model](https://github.com/tburgess97/Planning-for-Drunks)** simulates 25 individual drunks leaving the pub and drunkenly walking home to their individual houses whilst tracking each drunks route home and plotting a density map.

It was produced for GEOG5990: Assignment 2 as part of MSc River Basin Dynamics and Management with GIS 

### Model Summary
**[The model](https://github.com/tburgess97/Planning-for-Drunks):**
- Is ran in the command prompt by the user
- Reads in a raster environment and identifies the locations of the central pub and encircling houses
- Displays the town plan, including pub and houses, as a pop-out figure
- Simulates drunks leaving the pub in a drunkenly manner (taking random steps) until every drunk reaches their individual house
- Records the frequency that each point on the map is passed through by a drunk 
- Plots the frequency data as a density map, displays the map as a pop-out and saves the data locally as a txt. file

## User Guide

### Repository Contents

**1. README.md:** README file containing the model documentation and the user guide

**2. Drunksmodel.py:** Core model code

**3. Drunksframework.py:** Drunk agent class code

**4. town.txt:** txt file containing the environment data for the town plan

**5. LICENSE:** MIT License

### List of Dependencies

The model requires the following packages to be installed locally:

- [matplotlib: v3.5.1](https://matplotlib.org/)


### Running the Model

- Download [the model repository](https://github.com/tburgess97/Planning-for-Drunks) (under: code -> Download ZIP) and extract to a local directory
- Navigate to the directory the model is stored locally within the command prompt 
- Install the packages required (as listed in the dependences above) locally using pip install:
  - At the command prompt: > python -m pip 
  - To install packages at the command prompt: > python -m pip install <package>
    - Where packages required for the model: 'matplotlib'
- Run the model from the command prompt using the command: python Drunksmodel.py 
  1. The model first returns a display of the pub and house locations as a pop-out figure, this should be closed to continue the model run
  2. The model then simulates the closing of the pub and the first drunk leaves
  3. The drunk walk home of the first drunk is simulated, with the drunk taking a random step (up, down, left or right) until they reach their own home 
  4. Once the first drunk is home, it is confirmed at the command line and the number of drunks at home is returned
  5. The second drunk then leaves the pub, drunkenly walks around and reaches their home and the process (step 3-4) is repeated until the 25th drunk is home
  6. The model then confirms that all drunks are safely home 
  7. A density map of is then displayed as a pop-out figure with colour bar to show the heat map of where drunks have been
  8. This density map is saved locally to the destination of the model as 'drunk_density_map.txt'
  9. Closing the density map pop-out figure then ends the model 
  

### Model Checks 

A series of checks have been left in the model code as commented out statements. To run the model with checks returned, the check statements should be uncommented:
- Line 59: Environment read in and appended to a 2D list 
- Line 67: The width and length of the environment to inform the display axis limits and the boundary condition for drunks 
- Line 112: A blank density map has been appended
- Line 137: That each individual drunk has a specific ID and an assigned house
- Line 141-142: That each individual drunk has starting coordinates inside the pub
- Line 156-157: That each drunk takes one random step at a time and to have the model run in real time (can take ca. 5-15 minutes when each step is printed until all drunks make it home


## Model Design, Development Process, Issues and Further Development 

  The model was developed primarily for GEOG5990: Assignment 2 as part of MSc River Basin Dynamics and Management with GIS. It was developed with the potential use in within town planning and social risk management. 

  The development process was broken down into distinct sections and developed in the following order; reading in a txt. file as the town plan and appending it to a 2D list, displaying the town plan and identifying and displaying the pub and house locations, creating a blank density map under the same spatial parameters as the town plan, initiating a Drunk class starting in the pub with a random move function and a density function to count the times a coordinate is passed over, assigning each drunk an individual ID and house number so each drunk stops and is recorded once reaching home, saving the density map as a local txt. file and displaying it as a heat map with an associated colour bar key, allowing the model to be run from the command prompt. The model was setup to be ran from the command prompt to improve the accessability of the model and its ease of use. The initial development plan included the model to be simulated and diplayed as an animation, however early on in the development it became clear that this would be significantly more computationaly intense and require the user to wait a significant time for each drunk to arrive home. As the main aim of the model was not to animate drunks but to simulate the drunks and produce a density map output, the model was developed to not animate and display the drunks walks home. Despite this, a way of running the spatial simulation of the drunks walk home in 'real-time' was developed and can be run by uncommenting lines 156-157, allowing a significantly less time-consuming option to view the drunk walk home simulation.
  
  Although the model is a very simple representation of drunk's movements between leaving a pub and getting home, it could be used as the basis of a more complex model that better represents 'pub goers' journeys home. A more representative movement of drunks could be developed and used within the Drunk class' move function, including preventing drunks from retracing their steps and/or with time becoming more sober and therefore more direct in their movement towards their home. A town plan based on a real-world urban area could be utilised within the model, for example rasterised data of aerial imagery of a town. Furthermore, areas that 'attract' drunks between the pub and their house could be incorporated in the model, for example takeaways could be added and their impact on routes examined using the density map. A significant improvement to the density map output would be the incorporation of the pub and houses displayed within the final density map. With significant further development the model could be used to inform town planning such as; examining the best location for a new pub that will result in the least impact of disorderly behviour, or assessing the best location for a new late night taxi rank to reduce noise pollution. Potential uses in social risk management include; examining hotspots of drunk and disordely behviour within an area, identify areas that should be targetted by increased police presence and/or street angels.
  

## Author
**Student ID:** 201466497, The University of Leeds

## License 
The repository is licensed under the [MIT License](https://github.com/tburgess97/ABM/blob/main/LICENSE)

## Acknowledgements and references
The model was developed independently by the author, building on the foundations learnt within https://www.geog.leeds.ac.uk/courses/computing/study/core-python/

Foundations of agent-based modelling were learnt with help from:
https://www.geog.leeds.ac.uk/courses/computing/study/core-python/
  
Command line argument source code was adapted from:
https://docs.python.org/3/library/argparse.html
