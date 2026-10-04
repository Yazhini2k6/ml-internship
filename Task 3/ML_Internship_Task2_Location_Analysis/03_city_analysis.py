import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")
data["City"] = data["City"].fillna("Unknown")
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors="coerce")

city_count = data["City"].value_counts().head(15)

print("CITY ANALYSIS")
print("-------------")
print("Top 15 cities by number of restaurants:")
print(city_count)

city_rating = (
    data.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

print("\nTop 15 cities by average rating:")
print(city_rating)

plt.figure(figsize=(10, 6))
city_count.sort_values().plot(kind="barh")
plt.title("Top Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "city_restaurant_count.png"))
plt.close()

print("\nChart saved to outputs/city_restaurant_count.png")
