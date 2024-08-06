<h1>3D Visualization of India and Sri Lanka States</h1>

## Description
This project visualizes the states of India and Sri Lanka in a 3D plot using Plotly. It includes interactive features such as light and dark mode toggles and range sliders for filtering states. The project incorporates a graphical user interface (GUI) built with Tkinter and PyQt5, enhancing user interaction and experience.
## Features
- **3D Visualization**: Displays geographical boundaries of states in India and Sri Lanka.
- **Light/Dark Mode**: Toggle between light and dark modes for better visibility.
- **Interactive Range Sliders**: Filter and focus on individual states or show all states together.
- **Multiple GeoJSON File Support**: Load and combine multiple GeoJSON files.
- **GUI Integration**: User-friendly interfaces built with Tkinter and PyQt5 for file selection and visualization controls.
## Installation
To run this project, you need to have Python installed along with the following libraries:
```bash
pip install geopandas plotly pyqt5 tkinter
Tkinter is typically included with Python, so no additional installation is required for it.
```
You also need to have Tkinter installed, which is usually included with Python.
## Usage
1. Clone this repository.
2. Ensure you have the required GeoJSON files.
3. Run the script using a Python interpreter.
```bash
python your_script_with_gui.py
```
4. Select the GeoJSON files for India and Sri Lanka when prompted.
5. Interact with the 3D plot using the range sliders and mode toggles.
## Code Structure
### Files and Directories
- `your_script.py`: Main script for loading data and creating the visualization.
- `README.md`: This file providing an overview of the project.
### Script Breakdown
- **File Selection**: Using Tkinter and PyQt5 to select multiple GeoJSON files.
- **Data Loading**: Loading and combining GeoJSON data.
- **3D Plotting**: Creating a 3D plot with Plotly, including interactive elements and styling.
- **Light/Dark Mode**: Adding buttons to toggle between light and dark modes.
- **Interactive Range Sliders**: Adding range sliders to filter and focus on individual states.
- **GUI Integration**:
  - **Tkinter**: Implement Tkinter for basic GUI elements and file dialogs.
  - **PyQt5**: Enhance the GUI with PyQt5 for advanced controls and styling.
- **Annotations**: Adding annotations for the current date and time.
- **Display Plot**: Show the 3D plot with interactive features within the GUI.

### Summary of the Code
1. **Import Libraries**: Import necessary libraries including json, geopandas, plotly.graph_objs, plotly.subplots, tkinter, PyQt5, and datetime.
2. **File Selection Functions**:
    - Tkinter: Define functions to use Tkinter for file selection.
    - PyQt5: Define functions to use PyQt5 for file dialogs and advanced GUI controls.
3. **Load GeoJSON Function**: Define a function to load and combine GeoJSON data from selected files.
4. **Create GeoDataFrames**: Create GeoDataFrames from the combined GeoJSON data.
5. **Extract State Names**: Extract state names for India and Sri Lanka from GeoJSON data.
6. **3D Plotting**: Use Plotly to create a 3D plot of state boundaries.
7. **Light/Dark Mode**: Define light and dark mode styles and add toggle buttons.
8. **Range Sliders**: Add range sliders to filter and focus on individual states.
9. **GUI Integration**:
    - **Tkinter**: Implement Tkinter elements for file selection and basic controls.
    - **PyQt5**: Implement PyQt5 elements for advanced GUI functionality and enhanced user experience.
10. **Annotations**: Add annotations for the current date and time.
11. **Display Plot**: Show the 3D plot with interactive features within the GUI.
# Feature Ideas for 3D Visualization Project

## Summary

Here are some ideas for features you can add to your 3D visualization project:

### 1. Population Data Integration
- **Description**: Display the population of each state when hovering over it in the 3D plot.
- **Implementation**: Load population data from a CSV file and merge it with the GeoDataFrame.

### 2. Temperature Data Integration
- **Description**: Show the current temperature for each state in the hover text.
- **Implementation**: Make API calls to Open-Meteo to get temperature data and include it in the plot.

### 3. Enhanced Interactivity with Tooltips
- **Description**: Include additional state information such as area, capital, or historical facts in tooltips.
- **Implementation**: Extend the GeoJSON properties and the hover text to include more data points.

### 4. Animation of Historical Data
- **Description**: Show historical population growth or temperature changes over time.
- **Implementation**: Use Plotly's animation capabilities to create a time-lapse effect.

### 5. User-Selectable Data Layers
- **Description**: Enable toggling between different data layers like population, temperature, and economic data.
- **Implementation**: Add buttons or checkboxes for users to select the desired data layers.

### 6. Advanced Filtering Options
- **Description**: Allow users to filter states based on criteria such as population range or temperature thresholds.
- **Implementation**: Use dropdown menus or sliders to set filter criteria.

### 7. Improved UI/UX Design
- **Description**: Make the visualization more user-friendly with better navigation, more intuitive controls, and a polished layout.
- **Implementation**: Use PyQt5's advanced layout options and Tkinter's basic controls for a balanced UI/UX design.

### 8. Integration with Dash for a Complete Web Application
- **Description**: Provide a web interface where users can interact with the 3D plot, select data layers, and apply filters.
- **Implementation**: Use Dash to create a web app that serves the 3D visualization.

