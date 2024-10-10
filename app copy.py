# Importations nécessaires
from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np

# Charger l'imputer, le scaler et le modèle
imputer = joblib.load("imputer.joblib")
scaler = joblib.load("scaler.joblib")
model = joblib.load("logistic_regression_model.joblib")

# Initialiser l'API
app = FastAPI()

# Route pour la racine ("/")
@app.get("/")
def read_root():
    return {"message": "Bienvenue à l'API de scoring"}

# Fonction pour calculer la classe en fonction du seuil
def get_prediction_label(probability, threshold=0.53):
    return "Accepted" if probability < threshold else "Rejected"

# Route API pour la prédiction
@app.post("/predict")
async def predict(features: dict):
    # Convertir les données en DataFrame
    X = pd.DataFrame([features])
    
    # Imputation
    quantitative_columns = X.select_dtypes(include=[np.number]).columns
    X[quantitative_columns] = imputer.transform(X[quantitative_columns])

    # Normalisation
    X = scaler.transform(X)

    # Prédiction
    prob = model.predict_proba(X)[:, 1]  # Probabilité de défaut (classe 1)
    
    # Calculer la classe
    label = get_prediction_label(prob[0], threshold=0.53)
    
    return {"probability": prob[0], "class": label}
