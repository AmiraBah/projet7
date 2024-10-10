# Importations nécessaires
from fastapi import FastAPI
import joblib
import pandas as pd
import logging

# Charger le pipeline complet renommé
pipeline = joblib.load("pipeline.joblib")

# Initialiser l'API
app = FastAPI()

## Route pour la racine ("/")
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
    
    # Utiliser le pipeline pour imputation, normalisation et prédiction
    prob = pipeline.predict_proba(X)[:, 1]  # Probabilité de défaut (classe 1)
    
    # Garder la probabilité exacte (pas d'arrondi)
    prob_precise = prob[0]
    
    # Calculer la classe
    label = get_prediction_label(prob_precise, threshold=0.53)
    
    # Retourner la probabilité exacte et la classe
    return {"probability": prob_precise, "class": label}