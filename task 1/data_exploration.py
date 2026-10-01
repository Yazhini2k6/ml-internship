import pandas as pd

ds = pd.read_csv("../dataset.csv") #dataset loading

print("First 5 rows:")  
print(ds.head()) #displays first 5 rows

print("\nNumber of rows and columns in the dataset:", ds.shape) #displays number of rows and columns

print("\nColumn names:", ds.columns) # displays the column names

 # displays numerical and categorical columns names:

print("\nNumerical columns:")
print(ds.select_dtypes(include="number").columns.tolist()) 

print("\nCategorical columns:")
print(ds.select_dtypes(include=["object", "str"]).columns.tolist())

print("\nDataset information: \n")
print(ds.info()) # displays all the datatypes, column names, and count of non-null in the entire dataset

print("\nMissing values:")
print(ds.isnull().sum())  # displays the missing values

print("\nNumber of duplicate rows:", ds.duplicated().sum()) # displays the number of duplicate rows

print("\nStatistical summary:\n")
print(ds.describe())  # displays mean, std, min, max, quartiles for numerical columns as a summary 

# Display unique categorical values:
print("\nUnique values in categorical columns:")

print("\nCities:\n")
print(ds["City"].unique())

print("\nCuisines:\n")
print(ds["Cuisines"].unique())

print("\nPrice range:\n", ds["Price range"].unique())

print("\nRating text:\n")
print(ds["Rating text"].unique())
