# app.py
import streamlit as st
import joblib
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load the saved model
model = joblib.load("iris_model.pkl")
iris = load_iris()

st.title("🌸 Iris Flower Classifier")
st.write("Enter flower features to predict its species.")

# Sidebar for input
st.sidebar.header("Enter Input Features")
def user_input():
    sepal_length = st.sidebar.slider("Sepal length (cm)", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("Sepal width (cm)", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("Petal length (cm)", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("Petal width (cm)", 0.1, 2.5, 0.2)
    data = {
        "sepal length (cm)": sepal_length,
        "sepal width (cm)": sepal_width,
        "petal length (cm)": petal_length,
        "petal width (cm)": petal_width
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Display input
st.subheader("Input Features")
st.write(input_df)

# Predict
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader("Prediction")
st.write(f"Predicted Species: **{iris.target_names[prediction[0]]}**")

st.subheader("Prediction Probabilities")
st.bar_chart(prediction_proba[0])

# Sample visual: Sepal length vs width
st.subheader("Sepal Feature Scatter Plot")
fig, ax = plt.subplots()
for i, label in enumerate(iris.target_names):
    ax.scatter(
        iris.data[iris.target == i, 0],
        iris.data[iris.target == i, 1],
        label=label
    )
ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.legend()
st.pyplot(fig)
