from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly
import plotly.express as px
import json

app = Flask(__name__)
df = None  # Global variable to store the dataframe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global df
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        columns = df.columns.tolist()
        return jsonify(columns)
    return "Invalid file format"

@app.route('/plot', methods=['POST'])
def plot():
    global df
    if df is None:
        return "No data available"
    
    data = request.get_json()
    x_column = data['x']
    y_column = data['y']

    fig = px.scatter(df, x=x_column, y=y_column)  # Example visualization
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)