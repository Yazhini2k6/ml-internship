import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")
data["Price range"] = pd.to_numeric(data["Price range"], errors="coerce")
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"], errors="coerce")

price_count = data["Price range"].value_counts().sort_index()

print("PRICE ANALYSIS")
print("--------------")
print("Restaurants by price range:")
print(price_count)

average_rating = data.groupby("Price range")["Aggregate rating"].mean()

print("\nAverage rating by price range:")
print(average_rating)

plt.figure(figsize=(8, 5))
price_count.plot(kind="bar")
plt.title("Restaurants by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "price_range_distribution.png"))
plt.close()

plt.figure(figsize=(8, 5))
average_rating.plot(kind="bar")
plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "price_range_rating.png"))
plt.close()

print("\nCharts saved to outputs/")
