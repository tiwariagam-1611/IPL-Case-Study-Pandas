IPL Data Analysis Pandas Pipeline Project

Project Overview

This project is an end-to-end IPL data analysis pipeline built using Python and Pandas.
The objective of the project is to simulate a real-world data workflow by performing data ingestion, cleaning, transformation, analysis, reporting, and export operations on IPL datasets.

The project uses two datasets:

1. matches.csv – contains match-level information
2. deliveries.csv – contains ball-by-ball IPL data

The complete workflow follows:

Ingest → Clean → Transform → Analyze → Report → Export

Project Goals

The main goals of this project are:

* Understand practical data pipeline development
* Perform real-world data cleaning and validation
* Merge and transform multiple datasets
* Generate cricket-based analytical insights
* Export processed outputs into CSV and Excel formats
* Practice structured Pandas operations and aggregations

Technologies Used

* Python
* Pandas
* NumPy
* OpenPyXL / ExcelWriter

Project Structure

project_folder/

│
├── data/
│   ├── matches.csv
│   └── deliveries.csv
│
├── tasks/
│   ├── task1_total_runs_per_match.py
│   ├── task2_team_runs.py
│   ├── task3_top_batters.py
│   ├── ...
│   └── task20_winning_analysis.py
│
├── output/
│   ├── runs_per_match.csv
│   ├── top_batters.csv
│   ├── strike_rate.csv
│   ├── economy.csv
│   ├── death_overs.csv
│   └── other exported files
│
├── main.py
├── requirements.txt
└── README.txt

Pipeline Stages

Stage 1 – Data Ingestion

* Loaded both IPL datasets using Pandas
* Inspected dataset structure
* Checked shape, columns, and data types

Stage 2 – Data Cleaning and Validation

* Checked missing values
* Verified match ID alignment between datasets
* Corrected inconsistent data types
* Prepared clean DataFrames for analysis

Stage 3 – Data Transformation

* Created derived columns such as total runs
* Standardized column names
* Merged deliveries and matches datasets
* Built a unified DataFrame for analytics

Stage 4 – Core Analysis

The project performs multiple IPL analyses including:

1. Total runs scored per match
2. Team-wise runs per match
3. Top 10 batters
4. Batter strike rates
5. Top bowlers by economy
6. Most consistent batters
7. Highest individual scores
8. Boundary analysis
9. Boundary percentage
10. Dot ball analysis
11. Runs per over
12. Powerplay analysis
13. Death over analysis
14. Inning-wise scoring comparison
15. Toss impact analysis
16. Player of the match contribution
17. Venue-wise analysis
18. City-wise scoring trends
19. Season-wise run trends
20. Winning team analysis

Stage 5 – Derived Insights

Generated important cricket insights such as:

* Most consistent batter
* Best death-over batting teams
* Highest scoring venues
* Strong powerplay teams
* Run-scoring trends across seasons

Stage 6 – Reporting

* Organized outputs into structured DataFrames
* Renamed columns for readability
* Sorted analytical outputs properly
* Prepared clean export-ready results

Stage 7 – Data Export

All outputs are exported as:

* Individual CSV files
* Combined Excel workbook containing multiple sheets

Example exported files:

* runs_per_match.csv
* top_batters.csv
* strike_rate.csv
* economy.csv
* team_scores.csv
* death_overs.csv

How to Run the Project

1. Install dependencies

pip install pandas numpy openpyxl

2. Place datasets inside the data folder

* matches.csv
* deliveries.csv

3. Run the main pipeline

python main.py

Outputs

After execution:

* Processed CSV files are generated inside the output folder
* Final Excel summary file is created

Key Learning Outcomes

By completing this project, the following concepts are learned:

* End-to-end data pipeline design
* Real-world dataset cleaning
* Data transformation using Pandas
* Aggregation and groupby operations
* Data merging and feature creation
* Analytical reporting
* Exporting structured analytical results

Dataset Reference

IPL Dataset Source:
[Kaggle IPL Complete Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020?utm_source=chatgpt.com)

Project Reference Details sourced from uploaded overview document. 
