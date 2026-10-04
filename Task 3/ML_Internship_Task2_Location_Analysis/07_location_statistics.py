import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")

data = pd.read_csv(DATA_FILE, encoding="utf-8")

data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors="coerce")
data["Price range"] = pd.to_numeric(data["Price range"], errors="coerce")
data = data.dropna(subset=["Latitude", "Longitude"])
data = data[(data["Latitude"] != 0) & (data["Longitude"] != 0)]

print("LOCATION STATISTICS")
print("-------------------")
print("\nTotal restaurants with valid coordinates:")
print(len(data))

print("\nRestaurants by country:")
print(data["Country Code"].value_counts().head(15))

print("\nRestaurants by city:")
print(data["City"].value_counts().head(15))

print("\nAverage rating by city:")
print(
    data.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

print("\nAverage price range by city:")
print(
    data.groupby("City")["Price range"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)
