# ML Internship Task 2 - Location-Based Restaurant Analysis

## Project Objective

This project performs location-based analysis on a restaurant dataset. The analysis focuses on restaurant distribution, cities, cuisines, price ranges, geographical coordinates, location statistics, and simple location-based insights.

## Dataset

The dataset is stored in:

`dataset/dataset.csv`

It contains information such as restaurant name, country, city, location, cuisine, average cost, services, price range, rating, and votes.

## Project Files

```text
ML_Internship_Task2_Location_Analysis/
│
├── dataset/
│   └── dataset.csv
│
├── outputs/
│   └── generated files appear here
│
├── 01_data_exploration.py
├── 02_preprocessing.py
├── 03_city_analysis.py
├── 04_cuisine_analysis.py
├── 05_price_analysis.py
├── 06_location_analysis.py
├── 07_location_statistics.py
├── 08_map_visualization.py
├── 09_insights.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Open PowerShell or Command Prompt inside the project folder and run:

```text
pip install -r requirements.txt
```

## Run Each File Independently

Every Python file can be run independently from the project folder.

```text
python 01_data_exploration.py
python 02_preprocessing.py
python 03_city_analysis.py
python 04_cuisine_analysis.py
python 05_price_analysis.py
python 06_location_analysis.py
python 07_location_statistics.py
python 08_map_visualization.py
python 09_insights.py
```

The files read the original dataset directly, so an earlier script does not have to be run first.

## Run the Complete Project

To run all analysis files together:

```text
python main.py
```

## Main Outputs

The analysis creates the following files inside `outputs/`:

- `cleaned_dataset.csv`
- `city_restaurant_count.png`
- `top_cuisines.png`
- `price_range_distribution.png`
- `price_range_rating.png`
- `restaurant_location_distribution.png`
- `restaurant_map.html`

## Analysis Covered

1. Dataset exploration
2. Data preprocessing
3. City-wise restaurant analysis
4. Cuisine analysis
5. Price range analysis
6. Geographical location analysis
7. Location statistics
8. Interactive map visualization
9. Location-based insights

## Note

The results are descriptive findings from the supplied dataset. They should not be treated as a complete representation of all restaurants in the real world.
