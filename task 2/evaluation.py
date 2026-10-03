import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = "data/restaurants.csv"

def clean_data(df):

    df = df.copy() # Makes a copy of the dataset before cleaning it

    # Fills missing text values and removes extra spaces
    for column in ["Restaurant Name", "City", "Cuisines"]:
        df[column] = df[column].fillna("Unknown").astype(str).str.strip()

    # Converts the required numerical columns
    df["Price range"] = pd.to_numeric(df["Price range"], errors="coerce")
    df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")
    df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce").fillna(0)

    return df


def generate_recommendations(df, cuisine, city, price_range, top_n=5):
    # Creates a separate copy for the recommendation calculation
    data = df.copy()

    # Combines restaurant information into one text field
    data["recommendation_text"] = (
        "city " + data["City"] +
        " cuisine " + data["Cuisines"] +
        " price " + data["Price range"].fillna(-1).astype(str)
    )

    # Converts the text information into TF-IDF features
    vectorizer = TfidfVectorizer(lowercase=True)
    matrix = vectorizer.fit_transform(data["recommendation_text"])

    # Converts the sample user preferences into the same feature space
    query_vector = vectorizer.transform(
        [f"city {city} cuisine {cuisine} price {price_range}"]
    )

    # Finds the similarity between the user and every restaurant
    data["similarity"] = cosine_similarity(query_vector, matrix).flatten()

    # Returns the highest similarity recommendations
    return data.sort_values(
        ["similarity", "Aggregate rating", "Votes"],
        ascending=[False, False, False],
    ).head(top_n)


def precision_at_k(recommendations, cuisine, city, price_range, min_rating, k):
    # Uses only the first K recommendations for evaluation
    recommendations = recommendations.head(k)

    if recommendations.empty:
        return 0.0

    # Marks a recommendation as relevant when it satisfies the selected user preference criteria
    relevant = (
        recommendations["Cuisines"].str.lower().str.contains(
            str(cuisine).lower(), na=False
        )
        & recommendations["City"].str.lower().eq(str(city).lower())
        & (recommendations["Price range"] == price_range)
        & (recommendations["Aggregate rating"] >= min_rating)
    )

    # Calculates the proportion of relevant recommendations
    return float(relevant.mean())


def main():
    print("=" * 60)
    print("RESTAURANT RECOMMENDATION EVALUATION")
    print("=" * 60)

    # Loads and cleans the dataset independently
    df = clean_data(pd.read_csv(DATA_PATH))

    # Sample user preferences used for testing the recommender
    cuisine = "Indian"
    city = "New Delhi"
    price_range = 2
    min_rating = 4.0
    k = 5

    # Generates the top recommendations for evaluation
    recommendations = generate_recommendations(
        df, cuisine, city, price_range, k
    )

    # Calculates Precision@K to check recommendation quality
    precision = precision_at_k(
        recommendations, cuisine, city, price_range, min_rating, k
    )

    print("\nEvaluation criteria:")
    print("Cuisine:", cuisine)
    print("City:", city)
    print("Price range:", price_range)
    print("Minimum rating:", min_rating)
    print("K:", k)

    print(f"\nPrecision@{k}: {precision:.3f}")

    # Explains what the calculated evaluation value means
    print(
        "\nPrecision@K = proportion of the top-K recommendations "
        "satisfying the chosen relevance criteria."
    )

    print("\nEvaluation completed successfully.")


if __name__ == "__main__":
    main()
