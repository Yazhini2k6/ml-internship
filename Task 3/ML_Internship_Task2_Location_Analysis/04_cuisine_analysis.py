import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")

data["Cuisines"] = data["Cuisines"].fillna("Unknown")
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors="coerce")

cuisine_list = []
for value in data["Cuisines"]:
    for cuisine in str(value).split(","):
        cuisine_list.append(cuisine.strip())

cuisine_counts = pd.Series(cuisine_list).value_counts().head(15)

print("CUISINE ANALYSIS")
print("----------------")
print("Top 15 cuisines:")
print(cuisine_counts)

plt.figure(figsize=(10, 6))
cuisine_counts.sort_values().plot(kind="barh")
plt.title("Top Cuisines in the Dataset")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "top_cuisines.png"))
plt.close()

expanded = data[["Cuisines", "Aggregate rating"]].copy()
expanded["Cuisine"] = expanded["Cuisines"].str.split(",")
expanded = expanded.explode("Cuisine")
expanded["Cuisine"] = expanded["Cuisine"].str.strip()

average_rating = (
    expanded.groupby("Cuisine")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(15)
)

print("\nHighest average-rated cuisines among the available records:")
print(average_rating)
print("\nChart saved to outputs/top_cuisines.png")
