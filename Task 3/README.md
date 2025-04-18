# Task 3: End-to-End Machine Learning Project – Iris Flower Classifier 🌸

## Objective
Build, train, and deploy a machine learning model to classify Iris flower species using a web interface.

---

## Dataset Used
- **Dataset**: Iris Dataset (built-in from `sklearn.datasets`)
- **Features**:
  - Sepal Length
  - Sepal Width
  - Petal Length
  - Petal Width
- **Classes**:
  - Setosa
  - Versicolor
  - Virginica

---

## ML Model Details
- **Algorithm**: Logistic Regression
- **Preprocessing**: StandardScaler for feature scaling
- **Training Accuracy**: Printed after model evaluation
- **Saved as**: `model.pkl` and `scaler.pkl` (using `pickle`)

---

## Web App Details
- **Framework**: Flask (Python)
- **Frontend**: HTML + CSS (styled form for input)
- **Function**: 
  - User inputs flower measurements.
  - Backend loads the model and scaler.
  - Prediction is displayed on the same page.

---

## Project Structure

```
Task-3/
├── model.pkl              - trained model
├── scaler.pkl             - scaler for preprocessing
├── iris_model.ipynb       - Google Colab training notebook
├── app.py                 - Flask Python file
├── templates/             - folder needed by Flask
│   └── index.html         - HTML frontend
└── README.md              - correct information of whole project
```

## How to Run the App
1. Train the model using `iris_model.ipynb` if needed (or use existing `model.pkl`).
2. Make sure `index.html` is inside a folder named `templates/`.
3. In the same folder as `app.py`, run the following:
```bash
python app.py

4. Open browser and go to http://127.0.0.1:5000/

## Output

![task3_image1](https://github.com/user-attachments/assets/6b947e72-7b16-4435-91a7-70b6ebfeca4d)

![task3_image2](https://github.com/user-attachments/assets/1c69473b-8acd-4fc3-b160-87f214c37887)

![task3_image3](https://github.com/user-attachments/assets/5dae2bbc-ceec-4091-9845-c157a6c667e8)

## Tools & Libraries Used
- Python
- Scikit-learn
- Pandas & NumPy
- Flask
- HTML/CSS
- Pickle

## Conclusion
This task demonstrates a complete end-to-end ML workflow — from data preprocessing and model training to deployment via a Flask web app. The interactive UI makes it easy for users to classify Iris flowers based on input features.
