# app_streamlit.py
import streamlit as st
import requests

# Titre de l'application
st.title("Prédiction de défaut de crédit")

# Saisie des données par l'utilisateur
CC_CNT_DRAWINGS_ATM_CURRENT_MEAN = st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_MEAN", value=0.0, format="%.2f")
CC_CNT_DRAWINGS_CURRENT_MAX = st.number_input("CC_CNT_DRAWINGS_CURRENT_MAX", value=0.0, format="%.2f")
BURO_DAYS_CREDIT_MEAN = st.number_input("BURO_DAYS_CREDIT_MEAN", value=0.0, format="%.2f")
CC_AMT_BALANCE_MEAN = st.number_input("CC_AMT_BALANCE_MEAN", value=0.0, format="%.2f")
DAYS_BIRTH = st.number_input("DAYS_BIRTH (jours)", value=0)
PREV_NAME_CONTRACT_STATUS_Refused_MEAN = st.number_input("PREV_NAME_CONTRACT_STATUS_Refused_MEAN", value=0.0, format="%.2f")
BURO_CREDIT_ACTIVE_Active_MEAN = st.number_input("BURO_CREDIT_ACTIVE_Active_MEAN", value=0.0, format="%.2f")
DAYS_EMPLOYED = st.number_input("DAYS_EMPLOYED (jours)", value=0.0, format="%.2f")
REFUSED_DAYS_DECISION_MAX = st.number_input("REFUSED_DAYS_DECISION_MAX (jours)", value=0.0, format="%.2f")
CC_AMT_BALANCE_MIN = st.number_input("CC_AMT_BALANCE_MIN", value=0.0, format="%.2f")
ACTIVE_DAYS_CREDIT_MEAN = st.number_input("ACTIVE_DAYS_CREDIT_MEAN", value=0.0, format="%.2f")
CC_CNT_DRAWINGS_ATM_CURRENT_MAX = st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_MAX", value=0.0, format="%.2f")
CC_MONTHS_BALANCE_MEAN = st.number_input("CC_MONTHS_BALANCE_MEAN", value=0.0, format="%.2f")
BURO_STATUS_1_MEAN_MEAN = st.number_input("BURO_STATUS_1_MEAN_MEAN", value=0.0, format="%.2f")
CC_CNT_DRAWINGS_ATM_CURRENT_VAR = st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_VAR", value=0.0, format="%.2f")
REGION_RATING_CLIENT_W_CITY = st.number_input("REGION_RATING_CLIENT_W_CITY", value=0)
CC_AMT_DRAWINGS_CURRENT_MEAN = st.number_input("CC_AMT_DRAWINGS_CURRENT_MEAN", value=0.0, format="%.2f")
NAME_INCOME_TYPE_Working = st.number_input("NAME_INCOME_TYPE_Working", value=0)  # Utiliser 0 ou 1
PREV_NAME_PRODUCT_TYPE_walk_in_MEAN = st.number_input("PREV_NAME_PRODUCT_TYPE_walk_in_MEAN", value=0.0, format="%.2f")
PREV_CODE_REJECT_REASON_SCOFR_MEAN = st.number_input("PREV_CODE_REJECT_REASON_SCOFR_MEAN", value=0.0, format="%.2f")
DAYS_LAST_PHONE_CHANGE = st.number_input("DAYS_LAST_PHONE_CHANGE (jours)", value=0.0, format="%.2f")
APPROVED_DAYS_DECISION_MIN = st.number_input("APPROVED_DAYS_DECISION_MIN (jours)", value=0.0, format="%.2f")
DAYS_ID_PUBLISH = st.number_input("DAYS_ID_PUBLISH (jours)", value=0)
REG_CITY_NOT_WORK_CITY = st.number_input("REG_CITY_NOT_WORK_CITY", value=0)  # Utiliser 0 ou 1
REFUSED_HOUR_APPR_PROCESS_START_MIN = st.number_input("REFUSED_HOUR_APPR_PROCESS_START_MIN (minutes)", value=0.0, format="%.2f")
CODE_GENDER = st.number_input("CODE_GENDER (0 = inconnu, 1 = homme, 2 = femme)", value=0)  # Utiliser 0, 1 ou 2
BURO_STATUS_C_MEAN_MEAN = st.number_input("BURO_STATUS_C_MEAN_MEAN", value=0.0, format="%.2f")
PREV_NAME_CONTRACT_STATUS_Approved_MEAN = st.number_input("PREV_NAME_CONTRACT_STATUS_Approved_MEAN", value=0.0, format="%.2f")
EXT_SOURCE_1 = st.number_input("EXT_SOURCE_1", value=0.0, format="%.2f")
EXT_SOURCE_2 = st.number_input("EXT_SOURCE_2", value=0.0, format="%.2f")
EXT_SOURCE_3 = st.number_input("EXT_SOURCE_3", value=0.0, format="%.2f")

# Bouton pour envoyer les données
if st.button("Prédire"):
    # Créer un dictionnaire avec les données saisies
    input_data = {
        "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": CC_CNT_DRAWINGS_ATM_CURRENT_MEAN,
        "CC_CNT_DRAWINGS_CURRENT_MAX": CC_CNT_DRAWINGS_CURRENT_MAX,
        "BURO_DAYS_CREDIT_MEAN": BURO_DAYS_CREDIT_MEAN,
        "CC_AMT_BALANCE_MEAN": CC_AMT_BALANCE_MEAN,
        "DAYS_BIRTH": DAYS_BIRTH,
        "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": PREV_NAME_CONTRACT_STATUS_Refused_MEAN,
        "BURO_CREDIT_ACTIVE_Active_MEAN": BURO_CREDIT_ACTIVE_Active_MEAN,
        "DAYS_EMPLOYED": DAYS_EMPLOYED,
        "REFUSED_DAYS_DECISION_MAX": REFUSED_DAYS_DECISION_MAX,
        "CC_AMT_BALANCE_MIN": CC_AMT_BALANCE_MIN,
        "ACTIVE_DAYS_CREDIT_MEAN": ACTIVE_DAYS_CREDIT_MEAN,
        "CC_CNT_DRAWINGS_ATM_CURRENT_MAX": CC_CNT_DRAWINGS_ATM_CURRENT_MAX,
        "CC_MONTHS_BALANCE_MEAN": CC_MONTHS_BALANCE_MEAN,
        "BURO_STATUS_1_MEAN_MEAN": BURO_STATUS_1_MEAN_MEAN,
        "CC_CNT_DRAWINGS_ATM_CURRENT_VAR": CC_CNT_DRAWINGS_ATM_CURRENT_VAR,
        "REGION_RATING_CLIENT_W_CITY": REGION_RATING_CLIENT_W_CITY,
        "CC_AMT_DRAWINGS_CURRENT_MEAN": CC_AMT_DRAWINGS_CURRENT_MEAN,
        "NAME_INCOME_TYPE_Working": NAME_INCOME_TYPE_Working,
        "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN": PREV_NAME_PRODUCT_TYPE_walk_in_MEAN,
        "PREV_CODE_REJECT_REASON_SCOFR_MEAN": PREV_CODE_REJECT_REASON_SCOFR_MEAN,
        "DAYS_LAST_PHONE_CHANGE": DAYS_LAST_PHONE_CHANGE,
        "APPROVED_DAYS_DECISION_MIN": APPROVED_DAYS_DECISION_MIN,
        "DAYS_ID_PUBLISH": DAYS_ID_PUBLISH,
        "REG_CITY_NOT_WORK_CITY": REG_CITY_NOT_WORK_CITY,
        "REFUSED_HOUR_APPR_PROCESS_START_MIN": REFUSED_HOUR_APPR_PROCESS_START_MIN,
        "CODE_GENDER": CODE_GENDER,
        "BURO_STATUS_C_MEAN_MEAN": BURO_STATUS_C_MEAN_MEAN,
        "PREV_NAME_CONTRACT_STATUS_Approved_MEAN": PREV_NAME_CONTRACT_STATUS_Approved_MEAN,
        "EXT_SOURCE_1": EXT_SOURCE_1,
        "EXT_SOURCE_2": EXT_SOURCE_2,
        "EXT_SOURCE_3": EXT_SOURCE_3
    }

    # Envoyer une requête à l'API
    response = requests.post("http://127.0.0.1:8000/predict/", json=input_data)

    if response.status_code == 200:
        prediction = response.json()
        st.success(f"Probabilité de défaut : {prediction['probability_of_default']:.4f}")
        st.success(f"Classe prédite : {'Accepté' if prediction['class'] == 1 else 'Refusé'}")
    else:
        st.error("Erreur lors de la prédiction.")

