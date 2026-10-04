import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "cleaned_dataset.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")

print("PREPROCESSING")
print("-------------")
print("Original shape:", data.shape)

if "index" in data.columns:
    data = data.drop("index", axis=1)

numeric_columns = [
    "Longitude",
    "Latitude",
    "Average Cost for two",
    "Price range",
    "Aggregate rating",
    "Votes"
]

for column in numeric_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

data.loc[data["Longitude"] == 0, "Longitude"] = pd.NA
data.loc[data["Latitude"] == 0, "Latitude"] = pd.NA

text_columns = data.select_dtypes(include="object").columns
for column in text_columns:
    data[column] = data[column].fillna("Unknown")

data = data.dropna(subset=["Longitude", "Latitude"])
data = data.drop_duplicates()

data.to_csv(OUTPUT_FILE, index=False)

print("Cleaned shape:", data.shape)
print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)

print("\nRemaining missing values:")
print(data.isnull().sum())
