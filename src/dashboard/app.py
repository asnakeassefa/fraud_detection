from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load the fraud dataset
fraud_data = pd.read_csv('../../data/fraud_data_preprocessed.csv')

@app.route('/api/summary', methods=['GET'])
def get_summary():
    total_transactions = len(fraud_data)
    fraud_cases = fraud_data[fraud_data['class'] == 1]
    fraud_percentage = len(fraud_cases) / total_transactions * 100

    summary = {
        'total_transactions': total_transactions,
        'fraud_cases': len(fraud_cases),
        'fraud_percentage': round(fraud_percentage, 2),
    }
    return jsonify(summary)

@app.route('/api/fraud_trends', methods=['GET'])
def get_fraud_trends():
    fraud_trends = fraud_data.groupby('signup_time')['class'].sum().reset_index()
    return jsonify(fraud_trends.to_dict(orient='records'))

@app.route('/api/fraud_geography', methods=['GET'])
def get_fraud_geography():
    geo_data = fraud_data.groupby('source_Direct')['class'].sum().reset_index()
    return jsonify(geo_data.to_dict(orient='records'))

@app.route('/api/device_browser', methods=['GET'])
def get_device_browser_data():
    device_browser_data = fraud_data.groupby(['browser_FireFox', 'browser_IE','browser_Opera','browser_Safari'])['class'].sum().reset_index()
    return jsonify(device_browser_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)