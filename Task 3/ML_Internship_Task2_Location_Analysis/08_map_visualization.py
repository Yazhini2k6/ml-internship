import os
import pandas as pd

try:
    import folium
except ImportError:
    print("Folium is not installed.")
    print("Install it using: pip install folium")
    raise SystemExit

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dataset", "dataset.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "restaurant_map.html")
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv(DATA_FILE, encoding="utf-8")
data["Longitude"] = pd.to_numeric(data["Longitude"], errors="coerce")
data["Latitude"] = pd.to_numeric(data["Latitude"], errors="coerce")
data = data.dropna(subset=["Longitude", "Latitude"])
data = data[(data["Longitude"] != 0) & (data["Latitude"] != 0)]

if data.empty:
    print("No valid location records were found.")
    raise SystemExit

center_lat = data["Latitude"].mean()
center_lon = data["Longitude"].mean()

restaurant_map = folium.Map(location=[center_lat, center_lon], zoom_start=2)

for _, row in data.head(1000).iterrows():
    popup_text = (
        "Restaurant: " + str(row["Restaurant Name"]) +
        "<br>City: " + str(row["City"]) +
        "<br>Rating: " + str(row["Aggregate rating"])
    )

    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=3,
        popup=popup_text,
        fill=True
    ).add_to(restaurant_map)

restaurant_map.save(OUTPUT_FILE)

print("MAP VISUALIZATION")
print("-----------------")
print("Interactive restaurant map created:")
print(OUTPUT_FILE)
print("The map uses up to 1000 valid-coordinate records for easier viewing.")
