import pandas as pd

DATA_PATH = "data/restaurants.csv"

def main():
    print("=" * 60)
    print("RESTAURANT DATA PREPROCESSING")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH) # dataset loading

    print(f"Original dataset shape: {df.shape}")

    print("\nMissing values before cleaning:")
    missing = df.isnull().sum() #check for missing values
    print(missing[missing > 0] if missing.any() else "No missing values.")

    # Fills missing cuisine values with values "Unknown"
    if "Cuisines" in df.columns:
        df["Cuisines"] = df["Cuisines"].fillna("Unknown")

    # Cleans the important text columns
    for column in ["Restaurant Name", "City", "Cuisines"]:
        if column in df.columns:
            df[column] = df[column].fillna("Unknown").astype(str).str.strip()

    # Converts important columns into numeric format
    for column in ["Price range", "Aggregate rating", "Votes"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Encodes City values into numerical values
    if "City" in df.columns:
        df["City_encoded"] = df["City"].astype("category").cat.codes

    # Encodes table booking and online delivery values as 1 and 0
    for source, target in [
        ("Has Table booking", "Table_booking_encoded"),
        ("Has Online delivery", "Online_delivery_encoded"),
    ]:
        if source in df.columns:
            df[target] = (
                df[source].astype(str).str.strip().str.lower()
                .map({"yes": 1, "no": 0}).fillna(-1).astype(int)
            )

    # Checks again for the missing values after preprocessing
    print("\nMissing values after cleaning:")
    remaining = df.isnull().sum()
    print(remaining[remaining > 0] if remaining.any() else "No missing values.")

    print(f"\nFinal dataset shape: {df.shape}")

    # Displays a few cleaned records to verify the preprocessing
    cols = [c for c in [
        "Restaurant Name", "City", "Cuisines", "Price range",
        "Aggregate rating", "City_encoded", "Table_booking_encoded",
        "Online_delivery_encoded"
    ] if c in df.columns]

    print("\nSample cleaned records:")
    print(df[cols].head().to_string(index=False))

    print("\nPreprocessing completed successfully.")


if __name__ == "__main__":
    main()
