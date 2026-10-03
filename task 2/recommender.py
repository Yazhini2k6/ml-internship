import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = "data/restaurants.csv"


def clean_data(df):
    # Makes a copy so the original dataframe is not changed directly
    df = df.copy()

    # Cleans the main text columns and fills missing values
    for column in ["Restaurant Name", "City", "Cuisines"]:
        df[column] = df[column].fillna("Unknown").astype(str).str.strip()

    # Converts the numerical columns into numeric format
    df["Price range"] = pd.to_numeric(df["Price range"], errors="coerce")
    df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")
    df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce").fillna(0)

    return df


def recommend_restaurants(
    df,
    cuisine="Indian",
    city="New Delhi",
    price_range=2,
    min_rating=4.0,
    top_n=5,
):
    # Makes a copy before creating new recommendation columns
    df = df.copy()

    # Combines important restaurant details into one text field so that the content-based model can compare restaurants
    df["recommendation_text"] = (
        "city " + df["City"] +
        " cuisine " + df["Cuisines"] +
        " price " + df["Price range"].fillna(-1).astype(str)
    )

    # Converts the restaurant text into TF-IDF numerical features
    vectorizer = TfidfVectorizer(lowercase=True)
    matrix = vectorizer.fit_transform(df["recommendation_text"])

    # Creates the same type of text representation for user preferences
    query = f"city {city} cuisine {cuisine} price {price_range}"
    query_vector = vectorizer.transform([query])

    # Calculates how similar each restaurant is to the user preferences
    df["similarity"] = cosine_similarity(query_vector, matrix).flatten()

    filtered = df.copy()

    # Filters restaurants according to the selected city
    if city:
        x = filtered[filtered["City"].str.lower() == str(city).lower()]
        if not x.empty:
            filtered = x

    # Filters restaurants according to the selected cuisine
    if cuisine:
        x = filtered[
            filtered["Cuisines"].str.lower().str.contains(
                str(cuisine).lower(), na=False
            )
        ]
        if not x.empty:
            filtered = x

    # Filters restaurants according to the selected price range
    if price_range is not None:
        x = filtered[filtered["Price range"] == price_range]
        if not x.empty:
            filtered = x

    # Keeps restaurants with the required minimum rating
    if min_rating is not None:
        x = filtered[filtered["Aggregate rating"] >= min_rating]
        if not x.empty:
            filtered = x

    # Sorts by similarity first, then rating and votes
    return filtered.sort_values(
        ["similarity", "Aggregate rating", "Votes"],
        ascending=[False, False, False],
    ).head(top_n)


def main():
    print("=" * 60)
    print("CONTENT-BASED RESTAURANT RECOMMENDER")
    print("=" * 60)

    # Loads and cleans the dataset independently
    df = clean_data(pd.read_csv(DATA_PATH))

    # Sample user preferences used to test the recommendation system
    preferences = {
        "cuisine": "Indian",
        "city": "New Delhi",
        "price_range": 2,
        "min_rating": 4.0,
        "top_n": 5,
    }

    print("\nUser preferences:")
    for key, value in preferences.items():
        print(f"{key}: {value}")

    # Generates recommendations based on the sample preferences
    results = recommend_restaurants(df, **preferences)

    print("\nRecommended restaurants:")

    if results.empty:
        print("No matching restaurants found.")
    else:
        # Selects only the useful columns for displaying recommendations
        cols = [c for c in [
            "Restaurant Name", "City", "Cuisines", "Price range",
            "Aggregate rating", "Votes", "similarity"
        ] if c in results.columns]
        print(results[cols].to_string(index=False))

    print("\nRecommendation system completed successfully.")


if __name__ == "__main__":
    main()
