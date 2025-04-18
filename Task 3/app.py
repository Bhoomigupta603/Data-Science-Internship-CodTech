from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        sl = float(request.form["sepal_length"])
        sw = float(request.form["sepal_width"])
        pl = float(request.form["petal_length"])
        pw = float(request.form["petal_width"])
        
        data = np.array([[sl, sw, pl, pw]])
        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)[0]

        classes = ["Setosa", "Versicolor", "Virginica"]
        result = f"The predicted Iris flower is: {classes[prediction]}"
            
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
