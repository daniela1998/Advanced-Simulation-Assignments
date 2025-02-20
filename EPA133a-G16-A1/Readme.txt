# Advanced-Simulation-Assignment 1 Group 16

The following submission is provided with the following structure:
Structure inside this ZIP file: 

Folder EPA133a-G16-A1
  Subfolder "infrastructure"
  Subfolder "original"
    BMMS_overview.xlsx
     _roads.tsv
  Subfolder "cleaned"
    -_roads.tsv
    -road_transposed.csv
    -BMMS_overview_cleaned_prelim.xlsx
    -BMMS_overview_cleaned_bridges_after_LPRE_removed.xlsx
    -BMMS_overview.xlsx
  README.txt
  Report.pdf
  CleanRoads.ipynb
  CleanBridges..ipynb
  
  HOW TO RUN the code: 

 First, run the program CleanRoads.ipynb. 
Inputs:  _roads.tsv from the "original" folder 
Outputs:  1. new file called _roads.tsv and road_transposed.csv in the "infrastructure" folder. 

Secondly, run the program CleanBridges.ipynb
Inputs: the BMMS_overview.xlsx from the “original” folder  
The road_transposed.csv from the "cleaned" folder, created by CleanRoads.py
Outputs:  This program outputs intermediate and final results in xlsx files.

1. BMMS_overview_cleaned_prelim.xlsx
2. BMMS_overview_cleaned_bridges_after_LPRE_removed.xlsx
3. A new file called “BMMS_overview” in the "cleaned" folder. This is the final output.

  Lastly, please make sure to attach the files _roads.tsv and BMMS_overview.xlsx into the folder with the relative path: \WBSIM_Lab1_2024\infrastructure. 

