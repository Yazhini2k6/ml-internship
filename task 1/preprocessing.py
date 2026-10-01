import pandas as pd

ds = pd.read_csv("../dataset.csv")

print("First five records of the dataset:")
print(ds.head()) # displays first 5 rows
print("\nNumber of rows and columns in the dataset:", ds.shape) # displays number of rows and columns   
print("\nDuplicate records in the dataset:",ds.duplicated().sum()) # checks for duplicate rows
print("\nMissing values in the dataset:\n") 
print(ds.isnull().sum()) # checks for missing values

ds.drop_duplicates()
ds["Cuisines"] = ds["Cuisines"].fillna("Unknown") # Fill up missing values in "Cuisines" columns with "Unknown" 

print("\nMissing values in the dataset after filling up the missing values:\n")
print(ds.isnull().sum()) #checks again for missing values after filling up the missing values.

ds.to_csv("../cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved successfully.") # saves the cleaned dataset

