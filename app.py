# Importations nécessaires
from fastapi import FastAPI
import joblib
import pandas as pd
import logging

# Charger le pipeline complet renommé
pipeline = joblib.load("pipeline.joblib")

# Initialiser l'API
app = FastAPI()

# Définir les noms de caractéristiques attendus
expected_features = [
    "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN",
    "CC_CNT_DRAWINGS_CURRENT_MAX",
    "BURO_DAYS_CREDIT_MEAN",
    "CC_AMT_BALANCE_MEAN",
    "DAYS_BIRTH",
    "PREV_NAME_CONTRACT_STATUS_Refused_MEAN",
    "BURO_CREDIT_ACTIVE_Active_MEAN",
    "DAYS_EMPLOYED",
    "REFUSED_DAYS_DECISION_MAX",
    "CC_AMT_BALANCE_MIN",
    "ACTIVE_DAYS_CREDIT_MEAN",
    "CC_CNT_DRAWINGS_ATM_CURRENT_MAX",
    "CC_MONTHS_BALANCE_MEAN",
    "BURO_STATUS_1_MEAN_MEAN",
    "CC_CNT_DRAWINGS_ATM_CURRENT_VAR",
    "REGION_RATING_CLIENT_W_CITY",
    "CC_AMT_DRAWINGS_CURRENT_MEAN",
    "NAME_INCOME_TYPE_Working",
    "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN",
    "PREV_CODE_REJECT_REASON_SCOFR_MEAN",
    "DAYS_LAST_PHONE_CHANGE",
    "APPROVED_DAYS_DECISION_MIN",
    "DAYS_ID_PUBLISH",
    "REG_CITY_NOT_WORK_CITY",
    "REFUSED_HOUR_APPR_PROCESS_START_MIN",
    "CODE_GENDER",
    "BURO_STATUS_C_MEAN_MEAN",
    "NAME_EDUCATION_TYPE_Higher_education",
    "PREV_NAME_CONTRACT_STATUS_Approved_MEAN",
    "EXT_SOURCE_1",
    "EXT_SOURCE_2",
    "EXT_SOURCE_3"
]

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
    # Vérifiez que toutes les caractéristiques attendues sont présentes
    missing_features = set(expected_features) - set(features.keys())
    if missing_features:
        return {"error": f"Missing features: {', '.join(missing_features)}"}, 400
    
    # Convertir les données en DataFrame avec les noms de colonnes
    X = pd.DataFrame([features], columns=expected_features)

    # Convertir en tableau NumPy pour la prédiction
    X_np = X.values
    
    # Utiliser le pipeline pour imputation, normalisation et prédiction
    prob = pipeline.predict_proba(X_np)[:, 1]  # Probabilité de défaut (classe 1)
    
    # Garder la probabilité exacte (pas d'arrondi)
    prob_precise = prob[0]
    
    # Calculer la classe
    label = get_prediction_label(prob_precise, threshold=0.53)
    
    # Retourner la probabilité exacte et la classe
    return {"probability": prob_precise, "class": label}
