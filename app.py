# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load("personality_model.joblib")

# Define route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Extract user responses
    user_responses = np.array(data["responses"]).reshape(1, -1)
    # Get predictions from the model
    prediction = model.predict(user_responses)
    probabilities = model.predict_proba(user_responses)

    # Construct a response
    response = {
        "prediction": prediction.tolist(),
        "probabilities": probabilities.tolist()
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
