# test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue à l'API de scoring"}

def test_predict_accepted():
    features = {
    "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": 1.125,
    "CC_CNT_DRAWINGS_CURRENT_MAX": 11.0,
    "BURO_DAYS_CREDIT_MEAN": -284.125,
    "CC_AMT_BALANCE_MEAN": 213.1825,
    "DAYS_BIRTH": -13804.0,
    "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": 0.5,
    "BURO_CREDIT_ACTIVE_Active_MEAN": 0.875,
    "DAYS_EMPLOYED": -1921.0,
    "REFUSED_DAYS_DECISION_MAX": -641.0,
    "CC_AMT_BALANCE_MIN": 2780.1,
    "ACTIVE_DAYS_CREDIT_MEAN": -256.2857142857143,
    "CC_CNT_DRAWINGS_ATM_CURRENT_MAX": 5.0,
    "CC_MONTHS_BALANCE_MEAN": -12.5,
    "BURO_STATUS_1_MEAN_MEAN": 0.0,
    "CC_CNT_DRAWINGS_ATM_CURRENT_VAR": 2.375,
    "REGION_RATING_CLIENT_W_CITY": 1.0,
    "CC_AMT_DRAWINGS_CURRENT_MEAN": 20961.376874999998,
    "NAME_INCOME_TYPE_Working": 1.0,
    "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN": 0.16666666666666666,
    "PREV_CODE_REJECT_REASON_SCOFR_MEAN": 0.0,
    "DAYS_LAST_PHONE_CHANGE": 0.0,
    "APPROVED_DAYS_DECISION_MIN": -721.0,
    "DAYS_ID_PUBLISH": -4046.0,
    "REG_CITY_NOT_WORK_CITY": 1.0,
    "REFUSED_HOUR_APPR_PROCESS_START_MIN": 17.0,
    "CODE_GENDER": 0.0,
    "BURO_STATUS_C_MEAN_MEAN": 0.109375,
    "NAME_EDUCATION_TYPE_Higher_education": 1.0,
    "PREV_NAME_CONTRACT_STATUS_Approved_MEAN": 0.3333333333333333,
    "EXT_SOURCE_1": 0.3201332934327508,
    "EXT_SOURCE_2": 0.2620426497366743,
    "EXT_SOURCE_3": 0.1841161559307151
}

    response = client.post("/predict", json=features)
    assert response.status_code == 200
    json_response = response.json()
    assert "probability" in json_response
    assert "class" in json_response
    assert json_response["class"] == "Accepted"  

def test_predict_rejected():
    features = {
    "CC_CNT_DRAWINGS_ATM_CURRENT_MEAN": 1.125,
    "CC_CNT_DRAWINGS_CURRENT_MAX": 11.0,
    "BURO_DAYS_CREDIT_MEAN": -284.125,
    "CC_AMT_BALANCE_MEAN": 213293.1825,
    "DAYS_BIRTH": -13804.0,
    "PREV_NAME_CONTRACT_STATUS_Refused_MEAN": 0.5,
    "BURO_CREDIT_ACTIVE_Active_MEAN": 0.875,
    "DAYS_EMPLOYED": -1921.0,
    "REFUSED_DAYS_DECISION_MAX": -641.0,
    "CC_AMT_BALANCE_MIN": 2780.1,
    "ACTIVE_DAYS_CREDIT_MEAN": -256.2857142857143,
    "CC_CNT_DRAWINGS_ATM_CURRENT_MAX": 5.0,
    "CC_MONTHS_BALANCE_MEAN": -12.5,
    "BURO_STATUS_1_MEAN_MEAN": 0.0,
    "CC_CNT_DRAWINGS_ATM_CURRENT_VAR": 2.375,
    "REGION_RATING_CLIENT_W_CITY": 1.0,
    "CC_AMT_DRAWINGS_CURRENT_MEAN": 20961.376874999998,
    "NAME_INCOME_TYPE_Working": 1.0,
    "PREV_NAME_PRODUCT_TYPE_walk_in_MEAN": 0.16666666666666666,
    "PREV_CODE_REJECT_REASON_SCOFR_MEAN": 0.0,
    "DAYS_LAST_PHONE_CHANGE": 0.0,
    "APPROVED_DAYS_DECISION_MIN": -721.0,
    "DAYS_ID_PUBLISH": -4046.0,
    "REG_CITY_NOT_WORK_CITY": 1.0,
    "REFUSED_HOUR_APPR_PROCESS_START_MIN": 17.0,
    "CODE_GENDER": 0.0,
    "BURO_STATUS_C_MEAN_MEAN": 0.109375,
    "NAME_EDUCATION_TYPE_Higher_education": 1.0,
    "PREV_NAME_CONTRACT_STATUS_Approved_MEAN": 0.3333333333333333,
    "EXT_SOURCE_1": 0.3201332934327508,
    "EXT_SOURCE_2": 0.2620426497366743,
    "EXT_SOURCE_3": 0.1841161559307151
}

    response = client.post("/predict", json=features)
    assert response.status_code == 200
    json_response = response.json()
    assert "probability" in json_response
    assert "class" in json_response
    assert json_response["class"] == "Rejected"  
