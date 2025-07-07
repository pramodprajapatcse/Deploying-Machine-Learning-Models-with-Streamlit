

---

```markdown
# 🌼 Iris Flower Classification - Streamlit ML App

This project demonstrates how to **train a machine learning model** using the Iris dataset and **deploy it via a Streamlit web application**.
## 🌐 Live Demo

👉 [https://deploying-machine-learning-models-with-app-nrfmo53qspbesewjaqg.streamlit.app/]

---

## 📁 Project Structure

```

streamlit\_ml\_app/
├── iris\_model.pkl         # Trained ML model
├── train\_model.py         # Script to train and save the model
├── app.py                 # Streamlit web application
├── requirements.txt       # Python dependencies
└── README.md              # Project overview

````

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit_ml_app.git
cd streamlit_ml_app
````

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit scikit-learn pandas matplotlib joblib
```

---

## 🧠 Train the Model

Run this command to train and save the model:

```bash
python train_model.py
```

This will generate `iris_model.pkl`.

---

## 🌐 Run the Streamlit App Locally

```bash
streamlit run app.py
```

Open browser at: [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deploy to Streamlit Cloud

### Steps:

1. Push this project to a **GitHub repository**.
2. Go to [https://share.streamlit.io](https://share.streamlit.io).
3. Click **"Create app"**, connect your repo, choose `app.py` as the entry point.
4. Deploy 🎉 (https://deploying-machine-learning-models-with-app-nrfmo53qspbesewjaqg.streamlit.app/)

> Ensure your GitHub repo includes `app.py`, `iris_model.pkl`, `requirements.txt`, and this `README.md`.

---

## 📦 Example `requirements.txt`

```
streamlit
scikit-learn
pandas
matplotlib
joblib
```

---

## 🔍 Features

* Input sepal/petal dimensions
* Predict Iris species using trained RandomForest model
* Bar chart of prediction probabilities
* Feature scatter plot for visualization

---

## 🧪 Dataset

Uses the classic **Iris dataset** provided by `scikit-learn`.

---

## 👨‍💻 Author

**Pramod Prajapat**
GitHub: [@pramodprajapatcse](https://github.com/pramodprajapatcse)

---


