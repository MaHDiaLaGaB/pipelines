import json

# Load the GeoJSON file
with open("big-enough.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

# Function to check if a feature is related to Libya
def is_libya(feature):
    if "properties" in feature:
        # Extract relevant fields and check if they contain 'Libya'
        start_country = feature["properties"].get("StartCountry", "").lower()
        end_country = feature["properties"].get("EndCountry", "").lower()
        countries = feature["properties"].get("Countries", "").lower()

        return "libya" in {start_country, end_country, countries}

    return False

# Filter out only Libya-related features
filtered_features = [feature for feature in geojson_data["features"] if is_libya(feature)]

# Create new GeoJSON structure
filtered_geojson = {
    "type": "FeatureCollection",
    "features": filtered_features
}

# Save the filtered GeoJSON file
with open("filtered_data.geojson", "w", encoding="utf-8") as f:
    json.dump(filtered_geojson, f, indent=4)

print(f"Filtered GeoJSON saved with {len(filtered_features)} features.")
