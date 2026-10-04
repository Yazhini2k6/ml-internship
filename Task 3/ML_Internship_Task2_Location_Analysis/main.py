import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Restaurant Location-Based Analysis")
print("----------------------------------")
print("This program runs all analysis files one by one.")

scripts = [
    "01_data_exploration.py",
    "02_preprocessing.py",
    "03_city_analysis.py",
    "04_cuisine_analysis.py",
    "05_price_analysis.py",
    "06_location_analysis.py",
    "07_location_statistics.py",
    "08_map_visualization.py",
    "09_insights.py"
]

for script in scripts:
    print("\nRunning:", script)
    script_path = os.path.join(BASE_DIR, script)
    subprocess.run([sys.executable, script_path], check=True)

print("\nAll analysis files have been completed successfully.")
print("Check the outputs folder for charts, the cleaned dataset, and the map.")
