# README File

Created by: EPA133a Group 16

|    Name     | Student Number |
| :---------: | :------------- |
| Rachel Delvin Sutiono | 6284736        |
|  Celia Martínez Sillero  | 6222102         |
| Daniela Ríos Mora | 6275486       |
| Thunchanok Phutthaphaiboon| 6141153        |
| Yao Wang | 6157513         |



## Introduction

In the folder (EPA133a-G16-A2),  can find place group 16's lab submission for the Assignment 2.

This README file is to help a first-time user understand what it is about and how they might be able to use it.
If you are looking for information about the _model folder_ of Assignment 2, please navigate to the [model/README.md](model/README.md) in the [model](model) directory. 

## Purpose and objective of this project

This assignment focuses on simulating vehicle travel times under different infrastructure conditions in Bangladesh. Using Mesa library, an agent-based modeling tool, we built a simulation model to study how bridge conditions impact driving time on the N1 road. 
We test the model under nine different scenarios (from 0 to 9). Each scenario has different probabilities for bridge failures. 
The model outputs the average travel time for each scenario. The results are visualized in a box plot to compare the average travel time under different scenarios.

## Structure

The following submission is provided with the following structure:
Structure inside this ZIP file: 

    Folder EPA133a-G16-A2
        Subfolder data
        Subfolder experiment
            -scenario0.csv
            -scenario1.csv
            -scenario2.csv
            -scenario3.csv
            -scenario4.csv
            -scenario5.csv
            -scenario6.csv
            -scenario7.csv
            -scenario8.csv

      Subfolder model
            Subfolder Continuous Space
                -continuous_space.py
                -continuous_space_viz.py
            -model.py
            -components.py
            -model_viz.py
            -exploring.py
            -model_run.py
            -requirements.txt
            -Visualisation.ipynb
            -README.md
      Subfolder report
            -EPA133a-G16-A1-Report.pdf
      -README.md (this file)




## How to Use

The main file for the user to get the results is [model_run.py](model/model_run.py). This file contains the code to run the simulation model without visualization. 

1. Run model_run.py to get the results of the simulation. The results of each step will be printed in the console. 
2. To visualize the results: run the [Visualisation.ipynb](model/Visualisation.ipynb) file. This file contains the code to visualize the boxplot of the nine scenarios.


Please, keep in mind that the computational time to run the 9 scenarios is long. You can find attached the results of the simulation in the [experiment](experiment) folder. 





