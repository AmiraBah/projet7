import streamlit as st
import requests
import numpy as np

st.title("Client Default Prediction")

# Formulaire pour entrer les caractéristiques du client
features = {}
features['CC_CNT_DRAWINGS_ATM_CURRENT_MEAN'] = st.number_input('CC_CNT_DRAWINGS_ATM_CURRENT_MEAN', format="%.2f")
features['CC_CNT_DRAWINGS_CURRENT_MAX'] = st.number_input('CC_CNT_DRAWINGS_CURRENT_MAX', format="%.2f")
features['BURO_DAYS_CREDIT_MEAN'] = st.number_input('BURO_DAYS_CREDIT_MEAN', format="%.2f")
features['CC_AMT_BALANCE_MEAN'] = st.number_input('CC_AMT_BALANCE_MEAN', format="%.2f")
features['DAYS_BIRTH'] = st.number_input('DAYS_BIRTH', format="%d")
features['PREV_NAME_CONTRACT_STATUS_Refused_MEAN'] = st.number_input('PREV_NAME_CONTRACT_STATUS_Refused_MEAN', format="%.2f")
features['BURO_CREDIT_ACTIVE_Active_MEAN'] = st.number_input('BURO_CREDIT_ACTIVE_Active_MEAN', format="%.2f")
features['DAYS_EMPLOYED'] = st.number_input('DAYS_EMPLOYED', format="%.2f")
features['REFUSED_DAYS_DECISION_MAX'] = st.number_input('REFUSED_DAYS_DECISION_MAX', format="%.2f")
features['CC_AMT_BALANCE_MIN'] = st.number_input('CC_AMT_BALANCE_MIN', format="%.2f")
features['ACTIVE_DAYS_CREDIT_MEAN'] = st.number_input('ACTIVE_DAYS_CREDIT_MEAN', format="%.2f")
features['CC_CNT_DRAWINGS_ATM_CURRENT_MAX'] = st.number_input('CC_CNT_DRAWINGS_ATM_CURRENT_MAX', format="%.2f")
features['CC_MONTHS_BALANCE_MEAN'] = st.number_input('CC_MONTHS_BALANCE_MEAN', format="%.2f")
features['BURO_STATUS_1_MEAN_MEAN'] = st.number_input('BURO_STATUS_1_MEAN_MEAN', format="%.2f")
features['CC_CNT_DRAWINGS_ATM_CURRENT_VAR'] = st.number_input('CC_CNT_DRAWINGS_ATM_CURRENT_VAR', format="%.2f")
features['REGION_RATING_CLIENT_W_CITY'] = st.number_input('REGION_RATING_CLIENT_W_CITY', format="%d")
features['CC_AMT_DRAWINGS_CURRENT_MEAN'] = st.number_input('CC_AMT_DRAWINGS_CURRENT_MEAN', format="%.2f")
features['NAME_INCOME_TYPE_Working'] = st.selectbox('NAME_INCOME_TYPE_Working', options=[0, 1])  # 0 for other types, 1 for Working
features['PREV_NAME_PRODUCT_TYPE_walk-in_MEAN'] = st.number_input('PREV_NAME_PRODUCT_TYPE_walk-in_MEAN', format="%.2f")
features['PREV_CODE_REJECT_REASON_SCOFR_MEAN'] = st.number_input('PREV_CODE_REJECT_REASON_SCOFR_MEAN', format="%.2f")
features['DAYS_LAST_PHONE_CHANGE'] = st.number_input('DAYS_LAST_PHONE_CHANGE', format="%.2f")
features['APPROVED_DAYS_DECISION_MIN'] = st.number_input('APPROVED_DAYS_DECISION_MIN', format="%.2f")
features['DAYS_ID_PUBLISH'] = st.number_input('DAYS_ID_PUBLISH', format="%d")
features['REG_CITY_NOT_WORK_CITY'] = st.number_input('REG_CITY_NOT_WORK_CITY', format="%d")
features['REFUSED_HOUR_APPR_PROCESS_START_MIN'] = st.number_input('REFUSED_HOUR_APPR_PROCESS_START_MIN', format="%.2f")
features['CODE_GENDER'] = st.selectbox('CODE_GENDER', options=[0, 1])  # 0 for Female, 1 for Male
features['BURO_STATUS_C_MEAN_MEAN'] = st.number_input('BURO_STATUS_C_MEAN_MEAN', format="%.2f")
features['NAME_EDUCATION_TYPE_Higher education'] = st.selectbox('NAME_EDUCATION_TYPE_Higher education', options=[0, 1])  # 0 for other types, 1 for Higher education
features['PREV_NAME_CONTRACT_STATUS_Approved_MEAN'] = st.number_input('PREV_NAME_CONTRACT_STATUS_Approved_MEAN', format="%.2f")
features['EXT_SOURCE_1'] = st.number_input('EXT_SOURCE_1', format="%.2f")
features['EXT_SOURCE_2'] = st.number_input('EXT_SOURCE_2', format="%.2f")
features['EXT_SOURCE_3'] = st.number_input('EXT_SOURCE_3', format="%.2f")

# Bouton pour effectuer la prédiction
if st.button('Predict'):
    # URL de l'API Flask hébergée sur Render (ou une autre plateforme Cloud)
    api_url = "https://your-api-url.onrender.com/predict"
    
    # Faire une requête POST vers l'API
    response = requests.post(api_url, json={'features': list(features.values())})
    prediction = response.json()
    
    # Afficher les résultats
    st.write(f"Probability of Default: {prediction['probability']:.4f}")
    st.write(f"Prediction: {prediction['prediction']}")
