# Import necessary libraries
import pandas as pd
import numpy as np  # Add this line to import NumPy
from flask import Flask, jsonify, render_template

# Create Flask app
app = Flask(__name__)

# Function to generate pandas DataFrame with 'b' as modulo 10 of 'a'
def get_df():
    df = pd.DataFrame()
    df['a'] = np.random.randint(0, 101, size=1000)
    df['b'] = df['a'] % 10
    return df

# Route to return DataFrame data in JSON format
@app.route('/data')
def data():
    df = get_df()
    return jsonify(df.to_dict(orient='records'))

# Route to render HTML/JavaScript page
@app.route('/')
def index():
    return render_template('index.html')

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
