import json
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to load GeoJSON data from a file with explicit encoding
def load_geojson(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return json.load(f)
    except UnicodeDecodeError as e:
        print(f"Error reading the file {file_path} with encoding {encoding}: {e}")
        raise

# Function to save GeoJSON data to a file with explicit encoding
def save_geojson(data, file_path, encoding='utf-8'):
    try:
        with open(file_path, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=4)
    except UnicodeEncodeError as e:
        print(f"Error writing the file {file_path} with encoding {encoding}: {e}")
        raise

# Create a file dialog to select the GeoJSON files
def select_geojson_file(title):
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = askopenfilename(
        title=title,
        filetypes=[("GeoJSON Files", "*.geojson"), ("All Files", "*.*")]
    )
    return file_path

# Select the GeoJSON files
india_geojson_file_path = select_geojson_file("Select India GeoJSON File")
sri_lanka_geojson_file_path = select_geojson_file("Select Sri Lanka GeoJSON File")

if india_geojson_file_path and sri_lanka_geojson_file_path:
    # Load GeoJSON data from both files
    try:
        india_data = load_geojson(india_geojson_file_path)
        sri_lanka_data = load_geojson(sri_lanka_geojson_file_path)
    except UnicodeDecodeError:
        print("Failed to load one or both GeoJSON files due to encoding issues.")
        raise

    # Combine the features from both GeoJSON files
    combined_data = {
        "type": "FeatureCollection",
        "features": india_data.get('features', []) + sri_lanka_data.get('features', [])
    }

    # Create a file dialog to save the combined GeoJSON file
    combined_geojson_file_path = asksaveasfilename(
        title="Save Combined GeoJSON File",
        defaultextension=".geojson",
        filetypes=[("GeoJSON Files", "*.geojson"), ("All Files", "*.*")]
    )

    if combined_geojson_file_path:
        try:
            # Save the combined data to the new GeoJSON file
            save_geojson(combined_data, combined_geojson_file_path)
            print(f"Combined GeoJSON file saved as '{combined_geojson_file_path}'")
        except UnicodeEncodeError:
            print("Failed to save the combined GeoJSON file due to encoding issues.")
            raise
    else:
        print("No file selected for saving.")
else:
    print("No files selected.")
