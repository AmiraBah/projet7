import streamlit as st
import pandas as pd
import requests

# URL de l'API FastAPI 
API_URL = "http://127.0.0.1:8000/predict"

# Interface utilisateur Streamlit
st.title("Scoring de probabilité de défaut client")

# Option pour télécharger un fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV contenant les caractéristiques", type=["csv"])

if uploaded_file is not None:
    # Lire le fichier CSV
    df = pd.read_csv(uploaded_file)
    
    # Afficher les données pour vérification
    st.write("Données chargées :")
    st.dataframe(df)
    
    # Vérifier que les colonnes nécessaires sont présentes
    expected_features = [
        "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN", "CC_CNT_DRAWINGS_CURRENT_MAX", "BURO_DAYS_CREDIT_MEAN", 
        "CC_AMT_BALANCE_MEAN", "DAYS_BIRTH", "PREV_NAME_CONTRACT_STATUS_Refused_MEAN", 
        "BURO_CREDIT_ACTIVE_Active_MEAN", "DAYS_EMPLOYED", "REFUSED_DAYS_DECISION_MAX", 
        "CC_AMT_BALANCE_MIN", "ACTIVE_DAYS_CREDIT_MEAN", "CC_CNT_DRAWINGS_ATM_CURRENT_MAX", 
        "CC_MONTHS_BALANCE_MEAN", "BURO_STATUS_1_MEAN_MEAN", "CC_CNT_DRAWINGS_ATM_CURRENT_VAR", 
        "REGION_RATING_CLIENT_W_CITY", "CC_AMT_DRAWINGS_CURRENT_MEAN", "NAME_INCOME_TYPE_Working", 
        "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN", "PREV_CODE_REJECT_REASON_SCOFR_MEAN", 
        "DAYS_LAST_PHONE_CHANGE", "APPROVED_DAYS_DECISION_MIN", "DAYS_ID_PUBLISH", 
        "REG_CITY_NOT_WORK_CITY", "REFUSED_HOUR_APPR_PROCESS_START_MIN", "CODE_GENDER", 
        "BURO_STATUS_C_MEAN_MEAN", "NAME_EDUCATION_TYPE_Higher_education", 
        "PREV_NAME_CONTRACT_STATUS_Approved_MEAN", "EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3"
    ]

    missing_features = set(expected_features) - set(df.columns)
    if missing_features:
        st.error(f"Le fichier est manquant les colonnes suivantes : {', '.join(missing_features)}")
    else:
        # Bouton pour prédire
        if st.button("Prédire"):
            results = []
            for index, row in df.iterrows():
                # Convertir la ligne en dictionnaire
                features = row.to_dict()
                # Envoyer les données à l'API
                response = requests.post(API_URL, json=features)

                if response.status_code == 200:
                    result = response.json()
                    results.append({
                        "probability": result['probability'],
                        "class": result['class'],
                    })
                else:
                    st.error(f"Erreur dans la prédiction pour l'index {index}: {response.status_code}")
            
            # Afficher les résultats
            results_df = pd.DataFrame(results)
            st.write("Résultats des prédictions :")
            st.dataframe(results_df)
