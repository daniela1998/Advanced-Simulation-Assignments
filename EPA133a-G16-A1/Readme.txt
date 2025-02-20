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
    -BMMS_overview.xlsx
  README.txt
  Report.pdf
  CleanRoads.py
  CleanBridges.py
  
  HOW TO RUN the code: 

  First, run the program CleanRoads.py. This program reads the file _roads.tsv from the "original" folder and outputs new files called _roads.tsv and road_transposed.csv in the "infrastructure" folder. 
  Secondly, run the program CleanBridges.py. Following the previous methodology, this program will read the BMMS_overview.xlsx from the "folder" and create a new one with the same name in the "cleaned" folder. 
  Lastly, please make sure to attach the files _roads.tsv and BMMS_overview.xlsx into the folder with the relative path: \WBSIM_Lab1_2024\infrastructure 
