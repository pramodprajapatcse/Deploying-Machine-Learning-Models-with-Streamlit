# train_model.py

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Define model filename with full path
model_filename = os.path.join(os.getcwd(), 'iris_model.pkl')

# Save model
joblib.dump(model, model_filename)
print("✅ Model saved as:", model_filename)

# Debugging outputs
print("📁 File exists:", os.path.exists(model_filename))
print("📂 Current working directory:", os.getcwd())
print("📄 Files in directory:", os.listdir())
