import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")

data = pd.read_csv(DATA_FILE, encoding="utf-8")

print("DATA EXPLORATION")
print("----------------")
print("\nDataset shape:")
print(data.shape)

print("\nColumn names:")
print(list(data.columns))

print("\nFirst 5 rows:")
print(data.head())

print("\nMissing values:")
print(data.isnull().sum())

print("\nData types:")
print(data.dtypes)

print("\nBasic statistics:")
print(data.describe(include="all").transpose())
