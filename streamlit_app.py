import streamlit as st
import requests

# URL de l'API FastAPI (celle-ci fonctionne localement)
API_URL = "http://127.0.0.1:8000/predict"

# Interface utilisateur Streamlit
st.title("Scoring de probabilité de défaut client")

# Collecter les features avec des limites
features = {
    "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_MEAN", value=25.0, step=1.0),  # float
    "CC_CNT_DRAWINGS_CURRENT_MAX": st.number_input("CC_CNT_DRAWINGS_CURRENT_MAX", value=25.0, step=1.0),  # float
    "BURO_DAYS_CREDIT_MEAN": st.number_input("BURO_DAYS_CREDIT_MEAN", value=-1000.0, max_value=0.0, step=10.0),  # float
    "CC_AMT_BALANCE_MEAN": st.number_input("CC_AMT_BALANCE_MEAN", value=700000.0, step=100.0),  # float
    "DAYS_BIRTH": st.number_input("DAYS_BIRTH", value=-100.0, max_value=0.0, step=10.0),  # float
    "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": st.number_input("PREV_NAME_CONTRACT_STATUS_Refused_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "BURO_CREDIT_ACTIVE_Active_MEAN": st.number_input("BURO_CREDIT_ACTIVE_Active_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "DAYS_EMPLOYED": st.number_input("DAYS_EMPLOYED", value=-100.0, max_value=0.0, step=10.0),  # float
    "REFUSED_DAYS_DECISION_MAX": st.number_input("REFUSED_DAYS_DECISION_MAX", value=-100.0, max_value=0.0, step=10.0),  # float
    "CC_AMT_BALANCE_MIN": st.number_input("CC_AMT_BALANCE_MIN", value=10807.0, step=100.0),  # float
    "ACTIVE_DAYS_CREDIT_MEAN": st.number_input("ACTIVE_DAYS_CREDIT_MEAN", value=-100.0, max_value=0.0, step=10.0),  # float
    "CC_CNT_DRAWINGS_ATM_CURRENT_MAX": st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_MAX", value=4.0, min_value=0.0, step=1.0),  # float
    "CC_MONTHS_BALANCE_MEAN": st.number_input("CC_MONTHS_BALANCE_MEAN", value=-20.0, max_value=0.0, step=1.0),  # float
    "BURO_STATUS_1_MEAN_MEAN": st.number_input("BURO_STATUS_1_MEAN_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "CC_CNT_DRAWINGS_ATM_CURRENT_VAR": st.number_input("CC_CNT_DRAWINGS_ATM_CURRENT_VAR", value=2.0, min_value=0.0, max_value=3.0, step=0.1),  # float
    "REGION_RATING_CLIENT_W_CITY": st.number_input("REGION_RATING_CLIENT_W_CITY", value=2.0, min_value=0.0, max_value=3.0, step=0.1),  
    "CC_AMT_DRAWINGS_CURRENT_MEAN": st.number_input("CC_AMT_DRAWINGS_CURRENT_MEAN", value=13913.0, min_value=0.0, step=100.0),  # float
    "NAME_INCOME_TYPE_Working": st.number_input("NAME_INCOME_TYPE_Working", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN": st.number_input("PREV_NAME_PRODUCT_TYPE_walk_in_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "PREV_CODE_REJECT_REASON_SCOFR_MEAN": st.number_input("PREV_CODE_REJECT_REASON_SCOFR_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "DAYS_LAST_PHONE_CHANGE": st.number_input("DAYS_LAST_PHONE_CHANGE", value=-100.0, max_value=0.0, step=10.0),  # float
    "APPROVED_DAYS_DECISION_MIN": st.number_input("APPROVED_DAYS_DECISION_MIN", value=-100.0, max_value=0.0, step=10.0),  # float
    "DAYS_ID_PUBLISH": st.number_input("DAYS_ID_PUBLISH", value=-100.0, max_value=0.0, step=10.0),  # int
    "REG_CITY_NOT_WORK_CITY": st.selectbox("REG_CITY_NOT_WORK_CITY (0 = same, 1=different at city level)", [0, 1]),  # int
    "REFUSED_HOUR_APPR_PROCESS_START_MIN": st.number_input("REFUSED_HOUR_APPR_PROCESS_START_MIN", value=10.0, min_value=0.0, step=10.0),  # float
    "CODE_GENDER": st.selectbox("CODE_GENDER (0 = Female, 1 = Male)", [0, 1]),  # int
    "BURO_STATUS_C_MEAN_MEAN": st.number_input("BURO_STATUS_C_MEAN_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "NAME_EDUCATION_TYPE_Higher_education": st.number_input("NAME_EDUCATION_TYPE_Higher_education", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "PREV_NAME_CONTRACT_STATUS_Approved_MEAN": st.number_input("PREV_NAME_CONTRACT_STATUS_Approved_MEAN", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "EXT_SOURCE_1": st.number_input("EXT_SOURCE_1", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "EXT_SOURCE_2": st.number_input("EXT_SOURCE_2", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
    "EXT_SOURCE_3": st.number_input("EXT_SOURCE_3", value=0.5, min_value=0.0, max_value=1.0, step=0.1),  # float
}

# Lorsque l'utilisateur soumet le formulaire
if st.button("Prédire"):
    # Envoyer les données à l'API
    response = requests.post(API_URL, json=features)
    
    if response.status_code == 200:
        result = response.json()
        
        # Afficher la probabilité exacte renvoyée par l'API
        probability = result['probability']
        
        # Afficher le résultat avec la probabilité exacte et la classe
        st.write(f"**Probabilité de défaut** : {probability}")
        st.write(f"**Classe** : {result['class']}")
    else:
        st.write("Erreur dans la prédiction.")
        st.write(f"Code d'erreur : {response.status_code}")