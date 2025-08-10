# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load("model.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            values = [
                float(request.form["medinc"]),
                float(request.form["houseage"]),
                float(request.form["averooms"]),
                float(request.form["avebedrms"]),
                float(request.form["population"])
            ]
            prediction = model.predict(np.array([values]))[0]
            prediction = round(prediction * 100000, 2)
        except:
            prediction = "Invalid input"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
