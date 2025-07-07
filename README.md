
---

```markdown
# 🌼 Iris Flower Classification – Streamlit ML App

This project demonstrates how to **train a Machine Learning model** using the classic Iris dataset and **deploy it via a Streamlit web application** for real-time predictions.

---

## 🌐 Live Demo

👉 [Click here to try the live app](https://deploying-machine-learning-models-with-app-nrfmo53qspbesewjaqg.streamlit.app/)

---

## 📁 Project Structure

```

streamlit\_ml\_app/
├── iris\_model.pkl         # Trained ML model (RandomForest)
├── train\_model.py         # Script to train and save the model
├── app.py                 # Streamlit web app for predictions
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/streamlit_ml_app.git
cd streamlit_ml_app
````

### 2. Create a Virtual Environment (Optional but Recommended)


# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:


pip install streamlit scikit-learn pandas matplotlib joblib




## 🧠 Train the Model

To train the model and save it as a `.pkl` file:


python train_model.py


This will create a file named `iris_model.pkl` in the root directory.



## 💻 Run the Streamlit App Locally


streamlit run app.py


Then open your browser at [http://localhost:8501](http://localhost:8501).



## ☁️ Deploy to Streamlit Cloud

### Steps to Deploy:

1. Push the project to a **GitHub repository**.
2. Visit: [https://share.streamlit.io](https://share.streamlit.io)
3. Click **“Create app”**, connect your GitHub repo, and select `app.py` as the entry point.
4. Click **Deploy** 🎉

> Make sure your GitHub repository includes:
>
> * `app.py`
> * `iris_model.pkl`
> * `requirements.txt`
> * `README.md`



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

✅ Input Sepal and Petal dimensions
✅ Predict Iris species using a trained RandomForest model
✅ Visualize prediction probabilities as a bar chart
✅ Scatter plot visualization for better understanding

---

## 📊 Dataset

This project uses the classic **Iris dataset** provided by the `scikit-learn` library.
It includes measurements of sepal length, sepal width, petal length, and petal width for three species of Iris flowers:

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## 👨‍💻 Author

**Pramod Prajapat**
GitHub: [@pramodprajapatcse](https://github.com/pramodprajapatcse)

---
