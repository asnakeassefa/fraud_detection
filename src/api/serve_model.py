import os
from flask import Flask, request, jsonify
import joblib  # Assuming the model is saved using joblib
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)


model = joblib.load("../model.pkl")

@app.route("/")
def home():
    return jsonify({"message": "Fraud Detection API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        logging.info("Received request: %s", request.json)

        data = request.json
        features = data["features"]

        prediction = model.predict([features])

        logging.info("Prediction: %s", prediction[0])

        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        logging.error("Error: %s", str(e))
        return jsonify({"error": "Something went wrong"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
