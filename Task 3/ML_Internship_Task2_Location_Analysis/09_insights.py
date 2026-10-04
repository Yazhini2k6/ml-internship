import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")

data = pd.read_csv(DATA_FILE, encoding="utf-8")
data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors="coerce")
data = data.dropna(subset=["Latitude", "Longitude"])
data = data[(data["Latitude"] != 0) & (data["Longitude"] != 0)]

city_counts = data["City"].fillna("Unknown").value_counts()
average_city_rating = (
    data.groupby("City")["Aggregate rating"]
    .mean()
    .dropna()
    .sort_values(ascending=False)
)

most_common_cuisine = (
    data["Cuisines"]
    .fillna("Unknown")
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .index[0]
)

print("LOCATION-BASED INSIGHTS")
print("-----------------------")

if not city_counts.empty:
    highest_city_count = city_counts.index[0]
    highest_city_value = city_counts.iloc[0]
    print(
        "\n1. Restaurant concentration: "
        f"{highest_city_count} contains the largest number of records "
        f"({highest_city_value} restaurants)."
    )

if not average_city_rating.empty:
    highest_rating_city = average_city_rating.index[0]
    highest_rating_value = average_city_rating.iloc[0]
    print(
        "\n2. Average city rating: "
        f"{highest_rating_city} has the highest average rating in this "
        f"calculation ({highest_rating_value:.2f})."
    )

print(
    "\n3. Common cuisine: "
    f"{most_common_cuisine} is the most frequently listed cuisine."
)

print(
    "\n4. Coordinate coverage: "
    f"{len(data)} restaurants have usable latitude and longitude values."
)

print(
    "\n5. Geographic pattern: "
    "The scatter plot and interactive map can be used to observe "
    "restaurant clusters and compare restaurant concentration between "
    "different locations."
)

print(
    "\nNote: These are descriptive statistics from this dataset. "
    "They do not represent all restaurants in the real world."
)
