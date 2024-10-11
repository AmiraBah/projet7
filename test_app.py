from fastapi.testclient import TestClient
from app import app  # Assurez-vous que l'application FastAPI est importée correctement

client = TestClient(app)

# Test pour la route de la racine "/"
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue à l'API de scoring"}

# Test pour la route de prédiction "/predict" avec des données valides
def test_predict_valid():
    sample_features = {
    "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": 1.0,
    "CC_CNT_DRAWINGS_CURRENT_MAX": 11.0,
    "BURO_DAYS_CREDIT_MEAN": -284.0,
    "CC_AMT_BALANCE_MEAN": 213.0,
    "DAYS_BIRTH": -13804.0,
    "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": 0.5,
    "BURO_CREDIT_ACTIVE_Active_MEAN": 0.8,
    "DAYS_EMPLOYED": -1921.0,
    "REFUSED_DAYS_DECISION_MAX": -641.0,
    "CC_AMT_BALANCE_MIN": 2780.1,
    "ACTIVE_DAYS_CREDIT_MEAN": -256.0,
    "CC_CNT_DRAWINGS_ATM_CURRENT_MAX": 5.0,
    "CC_MONTHS_BALANCE_MEAN": -12.5,
    "BURO_STATUS_1_MEAN_MEAN": 0.0,
    "CC_CNT_DRAWINGS_ATM_CURRENT_VAR": 2.0,
    "REGION_RATING_CLIENT_W_CITY": 1.0,
    "CC_AMT_DRAWINGS_CURRENT_MEAN": 20961.0,
    "NAME_INCOME_TYPE_Working": 1.0,
    "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN": 0.2,
    "PREV_CODE_REJECT_REASON_SCOFR_MEAN": 0.0,
    "DAYS_LAST_PHONE_CHANGE": 0.0,
    "APPROVED_DAYS_DECISION_MIN": -721.0,
    "DAYS_ID_PUBLISH": -4046.0,
    "REG_CITY_NOT_WORK_CITY": 1.0,
    "REFUSED_HOUR_APPR_PROCESS_START_MIN": 17.0,
    "CODE_GENDER": 0.0,
    "BURO_STATUS_C_MEAN_MEAN": 0.1,
    "NAME_EDUCATION_TYPE_Higher_education": 1.0,
    "PREV_NAME_CONTRACT_STATUS_Approved_MEAN": 0.3,
    "EXT_SOURCE_1": 0.3,
    "EXT_SOURCE_2": 0.7,
    "EXT_SOURCE_3": 0.2
    }
    response = client.post("/predict", json=sample_features)
    assert response.status_code == 200
    data = response.json()
    assert "probability" in data
    assert "class" in data
    assert 0 <= data["probability"] <= 1

def test_predict_missing_features():
    incomplete_features = {
        "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": 1.0,
        "CC_CNT_DRAWINGS_CURRENT_MAX": 2.0,
        # Plusieurs autres caractéristiques manquent
    }
    
    # Appeler l'API avec des caractéristiques incomplètes
    response = client.post("/predict", json=incomplete_features)
    
    # Vérifier que le statut HTTP est bien 400 (Bad Request)
    assert response.status_code == 400
    
    # Extraire la réponse en JSON
    response_json = response.json()
    
    # Vérifier que la clé 'detail' existe dans la réponse
    assert "detail" in response_json
    
    # Vérifier que le contenu de 'detail' contient bien le message d'erreur attendu
    assert "Missing features" in response_json["detail"]
    
    # Optionnel : Vérifier que certaines des caractéristiques manquantes sont listées dans le message d'erreur
    missing_features_list = ["CC_CNT_DRAWINGS_ATM_CURRENT_VAR", "CC_AMT_DRAWINGS_CURRENT_MEAN"]
    for feature in missing_features_list:
        assert feature in response_json["detail"]  # Vérifier que chaque feature manquante est mentionnée dans 'detail'

