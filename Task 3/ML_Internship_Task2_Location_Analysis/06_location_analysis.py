import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")
data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
data = data.dropna(subset=["Longitude", "Latitude"])

data = data[(data["Longitude"] != 0) & (data["Latitude"] != 0)]

print("LOCATION ANALYSIS")
print("-----------------")
print("Number of restaurants with usable coordinates:", len(data))
print("\nLongitude range:")
print(data["Longitude"].min(), "to", data["Longitude"].max())
print("\nLatitude range:")
print(data["Latitude"].min(), "to", data["Latitude"].max())

plt.figure(figsize=(12, 7))
plt.scatter(data["Longitude"], data["Latitude"], s=8, alpha=0.5)
plt.title("Geographical Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "restaurant_location_distribution.png"))
plt.close()

print("\nChart saved to outputs/restaurant_location_distribution.png")
