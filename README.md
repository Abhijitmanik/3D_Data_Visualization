<h1>3D Visualization of India and Sri Lanka States</h1>

## Description
This project visualizes the states of India and Sri Lanka in a 3D plot using Plotly. It provides
interactive features such as light and dark mode toggles and range sliders for filtering states.
## Features
- **3D Visualization**: Displays geographical boundaries of states in India and Sri Lanka.
- **Light/Dark Mode**: Toggle between light and dark modes for better visibility.
- **Interactive Range Sliders**: Filter and focus on individual states or show all states together.
- **Multiple GeoJSON File Support**: Load and combine multiple GeoJSON files.
## Installation
To run this project, you need to have Python installed along with the following libraries:
```bash
pip install geopandas plotly
```
You also need to have Tkinter installed, which is usually included with Python.
## Usage
1. Clone this repository.
2. Ensure you have the required GeoJSON files.
3. Run the script using a Python interpreter.
```bash
python your_script.py
```
4. Select the GeoJSON files for India and Sri Lanka when prompted.
5. Interact with the 3D plot using the range sliders and mode toggles.
## Code Structure
### Files and Directories
- `your_script.py`: Main script for loading data and creating the visualization.
- `README.md`: This file providing an overview of the project.
### Script Breakdown
- **File Selection**: Using Tkinter to select multiple GeoJSON files.
- **Data Loading**: Loading and combining GeoJSON data.
- **3D Plotting**: Creating a 3D plot with Plotly, including interactive elements and styling.
- **Light/Dark Mode**: Adding buttons to toggle between light and dark modes.
- **Interactive Range Sliders**: Adding range sliders to filter and focus on individual states or show
all states together.
## Summary of the Code
1. **Import Libraries**: Import necessary libraries including `json`, `geopandas`, `plotly.graph_objs`,
`plotly.subplots`, `tkinter`, and `datetime`.
2. **File Selection Function**: Define a function to select multiple GeoJSON files using Tkinter.
3. **Load GeoJSON Function**: Define a function to load and combine GeoJSON data from
selected files.
4. **Create GeoDataFrames**: Create GeoDataFrames from the combined GeoJSON data.
5. **Extract State Names**: Extract state names for India and Sri Lanka from GeoJSON data.
6. **3D Plotting**: Use Plotly to create a 3D plot of state boundaries.
7. **Light/Dark Mode**: Define light and dark mode styles and add toggle buttons.
8. **Range Sliders**: Add range sliders to filter and focus on individual states.
9. **Annotations**: Add annotations for the current date and time.
10. **Display Plot**: Show the 3D plot with interactive features.

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
- **Implementation**: Use Plotly's advanced layout options and possibly integrate other libraries for enhanced UI elements.

### 8. Integration with Dash for a Complete Web Application
- **Description**: Provide a web interface where users can interact with the 3D plot, select data layers, and apply filters.
- **Implementation**: Use Dash to create a web app that serves the 3D visualization.

