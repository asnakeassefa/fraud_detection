# fraud_detection
This project is a fraud detection system. It uses a machine learning model to predict whether a transaction is fraudulent or not. The model is served through a Flask API, which can be accessed through a POST request to the /predict endpoint with the transaction details in the request body.

## Setup
To run this project, you need to have Python 3.8 or higher installed. You also need to install the required packages listed in the requirements.txt file. Once you have the dependencies installed, you can start the Flask server by running the serve_model.py script.

## Usage
Once the server is running, you can make a POST request to the /predict endpoint with the transaction details in the request body. The server will respond with a JSON object containing the prediction.

## Docker
This project also includes a Dockerfile for easy deployment. You can build the Docker image with the command `docker build -t fraud_detection .` and run it with the command `docker run -p 80:80 fraud_detection`.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.