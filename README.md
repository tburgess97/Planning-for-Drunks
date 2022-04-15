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


## Author
**Student ID:** 201466497, The University of Leeds

## License 
The repository is licensed under the [MIT License](https://github.com/tburgess97/ABM/blob/main/LICENSE)

## Acknowledgements
The model was developed independently by the author, building on the foundations learnt within https://www.geog.leeds.ac.uk/courses/computing/study/core-python/
