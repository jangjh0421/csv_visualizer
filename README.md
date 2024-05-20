
# CSV Visualizer Web Application

## Overview

CSV Visualizer is a web application designed to streamline the process of uploading, visualizing, and analyzing CSV data files. This application enables users to easily upload CSV files, select specific columns for plotting, and generate interactive visualizations using Plotly. The primary purpose of this web app is to improve efficiency in processing, visualizing, and analyzing massive raw data, specifically in the context of Canadian Urban Institution (CUI), where it serves as a valuable tool for data science research interns.

## Features

- **CSV File Upload**: Easily upload CSV files for processing.
- **Column Selection**: Select specific columns to plot on the X and Y axes.
- **Interactive Visualizations**: Generate interactive scatter plots using Plotly.
- **User-Friendly Interface**: Intuitive web interface for seamless interaction.

## Purpose

I created this web application primarily for my work as a data science research intern at Canadian Urban Institution (CUI). It aims to enhance my productivity by providing a convenient tool to handle and visualize large datasets, thereby facilitating better data-driven decision-making and research outcomes.

## Project Structure

```
csv_visualizer/
│
├── venv/               # Optional: Your virtual environment directory
│
├── app.py              # Main Flask application
├── requirements.txt    # List of dependencies
└── templates/
    └── index.html      # HTML template for the web interface
```

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/csv_visualizer.git
   cd csv_visualizer
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.**

## Usage

1. **Upload CSV File**: On the main page, use the file upload form to select and upload a CSV file.
2. **Select Columns**: Once the file is uploaded, dropdown menus will appear, allowing you to select the columns to be plotted on the X and Y axes.
3. **Generate Plot**: Click the "Plot" button to generate and display the interactive scatter plot.

## Dependencies

- Flask
- pandas
- plotly
