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
async def predict(features: Features):
    """
    Prédire la probabilité de défaut d'un client.

    - **features**: Un objet JSON contenant les caractéristiques du client.
    
    Renvoie un dictionnaire avec la probabilité et la classe.
    """
    # Convertir les données en DataFrame
    X = pd.DataFrame([features.dict()])  # Convertir l'objet Pydantic en dictionnaire
    
    # Imputation
    quantitative_columns = X.select_dtypes(include=[np.number]).columns
    X[quantitative_columns] = imputer.transform(X[quantitative_columns])

    # Normalisation
    X = scaler.transform(X)

    # Prédiction
    prob = model.predict_proba(X)[:, 1]  # Probabilité de défaut (classe 1)
    
    # Afficher la probabilité pour le débogage
    logging.info(f"Probability of default: {prob[0]}")

    # Calculer la classe
    label = get_prediction_label(prob[0], threshold=0.53)
    
    return {"probability": prob[0], "class": label}