import json
import os
import re

# Load your combined GeoJSON data
with open("only-all-ly.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

# Make sure output folder exists
os.makedirs("separated_pipelines", exist_ok=True)

def sanitize_filename(name):
    """Sanitize string to be a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "_", name).strip()

# Iterate through each pipeline feature
for feature in data["features"]:
    pipeline_name = feature["properties"].get("PipelineName", "unnamed_pipeline")
    safe_name = sanitize_filename(pipeline_name)

    # Build single-feature GeoJSON
    single_geojson = {
        "type": "FeatureCollection",
        "features": [feature]
    }

    # Write to file
    output_path = os.path.join("separated_pipelines", f"{safe_name}.geojson")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(single_geojson, f, indent=2)

    print(f"✅ Saved: {output_path}")
