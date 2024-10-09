# Importations nécessaires
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd

# Charger le modèle
pipeline = joblib.load("pipeline.joblib")

# Initialiser l'API
app = FastAPI()

# Route pour la racine (gère automatiquement les requêtes GET et HEAD)
@app.get("/")
async def read_root():
    return {"message": "Bienvenue sur l'API de prédiction de défaut"}

# Fonction pour calculer la classe en fonction du seuil
def get_prediction_label(probability, threshold=0.53):
    return "Accepted" if probability < threshold else "Rejected"

# Route API pour la prédiction
@app.post("/predict")
async def predict(features: dict):
    try:
        # Convertir les données en DataFrame pour les passer au modèle
        X = pd.DataFrame([features])
        
        # Prédiction
        prob = pipeline.predict_proba(X)[:, 1]  # Probabilité de défaut (classe 1)
        
        # Calculer la classe
        label = get_prediction_label(prob[0], threshold=0.53)
        
        return {"probability": prob[0], "class": label}
    
    except Exception as e:
        # Retourner une erreur HTTP 400 en cas de problème avec les données
        raise HTTPException(status_code=400, detail=f"Erreur lors de la prédiction : {str(e)}")
