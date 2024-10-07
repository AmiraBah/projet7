# app.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Charger le modèle depuis le fichier
model = joblib.load('model.joblib')  

class ClientData(BaseModel):
    CC_CNT_DRAWINGS_ATM_CURRENT_MEAN: float
    CC_CNT_DRAWINGS_CURRENT_MAX: float
    BURO_DAYS_CREDIT_MEAN: float
    CC_AMT_BALANCE_MEAN: float
    DAYS_BIRTH: int
    PREV_NAME_CONTRACT_STATUS_Refused_MEAN: float
    BURO_CREDIT_ACTIVE_Active_MEAN: float
    DAYS_EMPLOYED: float
    REFUSED_DAYS_DECISION_MAX: float
    CC_AMT_BALANCE_MIN: float
    ACTIVE_DAYS_CREDIT_MEAN: float
    CC_CNT_DRAWINGS_ATM_CURRENT_MAX: float
    CC_MONTHS_BALANCE_MEAN: float
    BURO_STATUS_1_MEAN_MEAN: float
    CC_CNT_DRAWINGS_ATM_CURRENT_VAR: float
    REGION_RATING_CLIENT_W_CITY: int
    CC_AMT_DRAWINGS_CURRENT_MEAN: float
    NAME_INCOME_TYPE_Working: int  # uint8 devient int pour une compatibilité Pydantic
    PREV_NAME_PRODUCT_TYPE_walk_in_MEAN: float
    PREV_CODE_REJECT_REASON_SCOFR_MEAN: float
    DAYS_LAST_PHONE_CHANGE: float
    APPROVED_DAYS_DECISION_MIN: float
    DAYS_ID_PUBLISH: int
    REG_CITY_NOT_WORK_CITY: int
    REFUSED_HOUR_APPR_PROCESS_START_MIN: float
    CODE_GENDER: int
    BURO_STATUS_C_MEAN_MEAN: float
    PREV_NAME_CONTRACT_STATUS_Approved_MEAN: float
    EXT_SOURCE_1: float
    EXT_SOURCE_2: float
    EXT_SOURCE_3: float

@app.post("/predict/")
async def predict(data: ClientData):
    input_data = np.array([[data.CC_CNT_DRAWINGS_ATM_CURRENT_MEAN,
                             data.CC_CNT_DRAWINGS_CURRENT_MAX,
                             data.BURO_DAYS_CREDIT_MEAN,
                             data.CC_AMT_BALANCE_MEAN,
                             data.DAYS_BIRTH,
                             data.PREV_NAME_CONTRACT_STATUS_Refused_MEAN,
                             data.BURO_CREDIT_ACTIVE_Active_MEAN,
                             data.DAYS_EMPLOYED,
                             data.REFUSED_DAYS_DECISION_MAX,
                             data.CC_AMT_BALANCE_MIN,
                             data.ACTIVE_DAYS_CREDIT_MEAN,
                             data.CC_CNT_DRAWINGS_ATM_CURRENT_MAX,
                             data.CC_MONTHS_BALANCE_MEAN,
                             data.BURO_STATUS_1_MEAN_MEAN,
                             data.CC_CNT_DRAWINGS_ATM_CURRENT_VAR,
                             data.REGION_RATING_CLIENT_W_CITY,
                             data.CC_AMT_DRAWINGS_CURRENT_MEAN,
                             data.NAME_INCOME_TYPE_Working,
                             data.PREV_NAME_PRODUCT_TYPE_walk_in_MEAN,
                             data.PREV_CODE_REJECT_REASON_SCOFR_MEAN,
                             data.DAYS_LAST_PHONE_CHANGE,
                             data.APPROVED_DAYS_DECISION_MIN,
                             data.DAYS_ID_PUBLISH,
                             data.REG_CITY_NOT_WORK_CITY,
                             data.REFUSED_HOUR_APPR_PROCESS_START_MIN,
                             data.CODE_GENDER,
                             data.BURO_STATUS_C_MEAN_MEAN,
                             data.PREV_NAME_CONTRACT_STATUS_Approved_MEAN,
                             data.EXT_SOURCE_1,
                             data.EXT_SOURCE_2,
                             data.EXT_SOURCE_3]])
    
    proba = model.predict_proba(input_data)[:, 1]
    class_label = (proba >= 0.5).astype(int)  # Utilisez le seuil optimal ici
    return {
        "probability_of_default": proba[0],
        "class": int(class_label[0])  # 0 pour refusé, 1 pour accepté
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
