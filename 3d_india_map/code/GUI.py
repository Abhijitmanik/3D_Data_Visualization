import json
import geopandas as gpd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from datetime import datetime
import os

def select_geojson_files(title="Select GeoJSON Files"):
    root = Tk()
    root.withdraw()  # Hide the root window
    file_paths = askopenfilenames(
        title=title,
        filetypes=[("GeoJSON Files", "*.geojson"), ("All Files", "*.*")]
    )
    return file_paths

def load_geojson(file_paths):
    combined_data = {'type': 'FeatureCollection', 'features': []}
    for file_path in file_paths:
        try:
            with open(file_path) as f:
                data = json.load(f)
                combined_data['features'].extend(data['features'])
                print(f"Loaded {file_path}")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    return combined_data

def create_3d_plot():
    try:
        # Select and load GeoJSON files
        geojson_file_paths_india = select_geojson_files("Select GeoJSON Files for India")
        geojson_file_paths_srilanka = select_geojson_files("Select GeoJSON Files for Sri Lanka")

        combined_data_india = load_geojson(geojson_file_paths_india)
        combined_data_srilanka = load_geojson(geojson_file_paths_srilanka)

        # Create GeoDataFrames from the combined GeoJSON data
        gdf_india = gpd.GeoDataFrame.from_features(combined_data_india['features'])
        gdf_srilanka = gpd.GeoDataFrame.from_features(combined_data_srilanka['features'])

        state_names_india = []
        state_names_srilanka = []
        trace_indices_india = []
        trace_indices_srilanka = []

        # Extract state names for India
        for feature in combined_data_india['features']:
            state_name = feature['properties'].get('NAME_1', feature['properties'].get('name', 'Unknown'))
            state_names_india.append(state_name)

        # Extract state names for Sri Lanka
        for feature in combined_data_srilanka['features']:
            state_name = feature['properties'].get('NAME_1', feature['properties'].get('name', 'Unknown'))
            state_names_srilanka.append(state_name)

        fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

        # Add traces for India
        for feature in combined_data_india['features']:
            coordinates = feature['geometry']['coordinates']
            state_name = feature['properties'].get('NAME_1', feature['properties'].get('name', 'Unknown'))

            if feature['geometry']['type'] == 'Polygon':
                x = [point[0] for point in coordinates[0]]
                y = [point[1] for point in coordinates[0]]
                z = [0] * len(x)  # Flat surface at z=0

                trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', name=state_name, showlegend=False, hoverinfo='name')
                fig.add_trace(trace)
                trace_indices_india.append(len(fig.data) - 1)

            elif feature['geometry']['type'] == 'MultiPolygon':
                for polygon in coordinates:
                    x = [point[0] for point in polygon[0]]
                    y = [point[1] for point in polygon[0]]
                    z = [0] * len(x)  # Flat surface at z=0

                    trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', name=state_name, showlegend=False, hoverinfo='name')
                    fig.add_trace(trace)
                    trace_indices_india.append(len(fig.data) - 1)

        # Add traces for Sri Lanka
        for feature in combined_data_srilanka['features']:
            coordinates = feature['geometry']['coordinates']
            state_name = feature['properties'].get('NAME_1', feature['properties'].get('name', 'Unknown'))

            if feature['geometry']['type'] == 'Polygon':
                x = [point[0] for point in coordinates[0]]
                y = [point[1] for point in coordinates[0]]
                z = [0] * len(x)  # Flat surface at z=0

                trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', name=state_name, showlegend=False, hoverinfo='name')
                fig.add_trace(trace)
                trace_indices_srilanka.append(len(fig.data) - 1)

            elif feature['geometry']['type'] == 'MultiPolygon':
                for polygon in coordinates:
                    x = [point[0] for point in polygon[0]]
                    y = [point[1] for point in polygon[0]]
                    z = [0] * len(x)  # Flat surface at z=0

                    trace = go.Scatter3d(x=x, y=y, z=z, mode='lines', name=state_name, showlegend=False, hoverinfo='name')
                    fig.add_trace(trace)
                    trace_indices_srilanka.append(len(fig.data) - 1)

        # Get current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")

        # Define light and dark modes
        light_mode = dict(
            paper_bgcolor='white',
            plot_bgcolor='white',
            font_color='black'
        )

        dark_mode = dict(
            paper_bgcolor='black',
            plot_bgcolor='black',
            font_color='white'
        )

        # Create range slider steps for India
        steps_india = []

        # Step for showing all Indian states
        step_all_india = dict(
            method="update",
            args=[{"visible": [i in trace_indices_india or i in trace_indices_srilanka for i in range(len(fig.data))]}],
            label="All Indian States"
        )
        steps_india.append(step_all_india)

        for state_index, state_name in enumerate(state_names_india):
            step = dict(
                method="update",
                args=[{"visible": [i in trace_indices_india and fig.data[i].name == state_name for i in range(len(fig.data))] + [False] * (len(fig.data) - len(trace_indices_india))}],
                label=state_name
            )
            steps_india.append(step)

        # Create range slider steps for Sri Lanka
        # steps_srilanka = []

        # # Step for showing all Sri Lankan states
        # step_all_srilanka = dict(
        #     method="update",
        #     args=[{"visible": [i in trace_indices_srilanka or i in trace_indices_india for i in range(len(fig.data))]}],
        #     label="All Sri Lankan States"
        # )
        # steps_srilanka.append(step_all_srilanka)

        # for state_index, state_name in enumerate(state_names_srilanka):
        #     step = dict(
        #         method="update",
        #         args=[{"visible": [i in trace_indices_srilanka and fig.data[i].name == state_name for i in range(len(fig.data))] + [False] * (len(fig.data) - len(trace_indices_srilanka))}],
        #         label=state_name
        #     )
        #     steps_srilanka.append(step)

        # Add annotations for date and time
        annotations = [
            dict(
                x=0.95,
                y=1.15,
                xref='paper',
                yref='paper',
                text=f'Date: {current_date}',
                showarrow=False,
                font=dict(size=12)
            ),
            dict(
                x=0.95,
                y=1.1,
                xref='paper',
                yref='paper',
                text=f'Time: {current_time}',
                showarrow=False,
                font=dict(size=12)
            ),
            dict(
                x=0.95,
                y=0,
                xref='paper',
                yref='paper',
                text='<b> Created  by Abhijit Manik </b>',
                showarrow=False,
                font=dict(size=12),
                align='right'
            )
        ]
        

        # Create a logo HTML snippet
        logo_html = '<img src="logo.png" style="position: absolute; top: 10px; left: 10px; width: 100px;"/>'

        # Update layout with range sliders, light/dark mode buttons, and annotations
        fig.update_layout(
            title={
                'text': '<b>3D Visualization of India and Sri Lanka</b>',
                'x': 0.5,  # Center align the title horizontally
                'y': 0.98,  # Position the title higher up on the y-axis
                'xanchor': 'center',
                'yanchor': 'top'
            },
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                aspectmode='auto'
            ),
            updatemenus=[
                dict(
                    type="buttons",
                    x=0.17,
                    xanchor="left",
                    y=1.15,
                    yanchor="top",
                    buttons=[
                        dict(label="Light Mode",
                             method="relayout",
                             args=[{"paper_bgcolor": light_mode['paper_bgcolor'],
                                    "plot_bgcolor": light_mode['plot_bgcolor'],
                                    "font.color": light_mode['font_color']}]
                             ),
                        dict(label="Dark Mode",
                             method="relayout",
                             args=[{"paper_bgcolor": dark_mode['paper_bgcolor'],
                                    "plot_bgcolor": dark_mode['plot_bgcolor'],
                                    "font.color": dark_mode['font_color']}]
                             )
                    ],
                    showactive=True
                )
            ],
            sliders=[{
                'steps': steps_india,
                'currentvalue': {'prefix': 'India States: '}
            }, 
            # {
            #     'steps': steps_srilanka,
            #     'currentvalue': {'prefix': 'Sri Lanka States: '}
            # }
            ],
            annotations=annotations
        )

        # Save the plot to an HTML file
        output_html_file = os.path.join(os.getcwd(), '3d_visualization.html')
        with open(output_html_file, 'w', encoding='utf-8') as file:
            file.write(logo_html)  # Write logo HTML to the file
            file.write(fig.to_html(full_html=False))  # Append plot HTML

 

        print(f"Visualization saved to {output_html_file}")

        return output_html_file

    except Exception as e:
        print(f"An error occurred: {e}")

class VisualizationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D Visualization")
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('logo.png'))  # Set the window icon

        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_visualization()

    def load_visualization(self):
        html_file = create_3d_plot()
        if html_file:
            self.web_view.setUrl(QUrl.fromLocalFile(html_file))

if __name__ == "__main__":
    app = QApplication([])
    window = VisualizationApp()
    window.show()
    app.exec_()

