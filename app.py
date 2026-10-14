import os
import random

from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your actual university registration number.
STUDENT_ROLL_NUMBER = "FA23-BDS-009"

# Generate deterministic coefficients.
random.seed(STUDENT_ROLL_NUMBER)

a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Linear Regression Prediction API is running",
        "endpoint": "/predict",
        "method": "GET",
        "parameters": ["x1", "x2", "x3"]
    })


@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])

        # Reject NaN and infinite input values.
        if not all(map(
            lambda value: value == value
            and abs(value) != float("inf"),
            [x1, x2, x3]
        )):
            return jsonify({
                "error": "Input values must be finite numbers"
            }), 400

        # Apply the linear regression equation.
        prediction = a1 * x1 + a2 * x2 + a3 * x3 + b

        return jsonify({
            "registration number": STUDENT_ROLL_NUMBER,
            "prediction": round(prediction, 2)
        })

    except KeyError:
        return jsonify({
            "error": "Please provide x1, x2 and x3"
        }), 400

    except ValueError:
        return jsonify({
            "error": "All input parameters must be numeric"
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
