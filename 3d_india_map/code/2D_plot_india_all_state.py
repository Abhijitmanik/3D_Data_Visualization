
import json
import geopandas as gpd
import plotly.graph_objs as go
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from datetime import datetime

# Step 1: Create a file dialog to select the GeoJSON file
def select_geojson_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = askopenfilename(
        title="Select GeoJSON File",
        filetypes=[("GeoJSON Files", "*.geojson"), ("All Files", "*.*")]
    )
    return file_path

# Step 2: Load GeoJSON data from the selected file
geojson_file_path = select_geojson_file()

if geojson_file_path:
    with open(geojson_file_path) as f:
        data = json.load(f)

    # Step 3: Create a GeoDataFrame from the GeoJSON data
    gdf = gpd.GeoDataFrame.from_features(data['features'])

    state_names = []

    # Step 4: Print state names and coordinates
    for feature in data['features']:
        state_name = feature['properties']['NAME_1']
        coordinates = feature['geometry']['coordinates']
        print(f"State: {state_name}")
        print(f"Coordinates: {coordinates}")
        state_names.append(state_name)

    # Step 5: Extract coordinates for plotting
    fig = go.Figure()

    for feature in data['features']:
        coordinates = feature['geometry']['coordinates']
        if feature['geometry']['type'] == 'Polygon':
            x = [point[0] for point in coordinates[0]]
            y = [point[1] for point in coordinates[0]]

            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=feature['properties']['NAME_1']))

        elif feature['geometry']['type'] == 'MultiPolygon':
            for polygon in coordinates:
                x = [point[0] for point in polygon[0]]
                y = [point[1] for point in polygon[0]]

                fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=feature['properties']['NAME_1']))

    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    fig.update_layout(
        title='GeoJSON Data in 2D',
        xaxis_title='Longitude',
        yaxis_title='Latitude',
        annotations=[
            dict(
                x=0.95,
                y=1.1,
                xref='paper',
                yref='paper',
                text=f'Date: {current_date}',
                showarrow=False,
                font=dict(size=12)
            ),
            dict(
                x=0.95,
                y=1.05,
                xref='paper',
                yref='paper',
                text=f'Time: {current_time}',
                showarrow=False,
                font=dict(size=12)
            )
        ],
        width=800,  # Set the width of the plot
        height=600,
        showlegend=False  # Set the height of the plot
    )

    fig.show()

else:
    print("No file selected.")
