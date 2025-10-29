from fastapi import APIRouter, Body

router = APIRouter(prefix='/risk-score', tags=["RiskScoring"])

@router.post('/predict')
def risk_score(data: dict = Body(...)):
    # data = {"age": 67, "diabetes": True, "hypertension": True, ...}
    score = int(data["age"]) + int(data["diabetes"]) * 10 + int(data["hypertension"]) * 10
    if score > 70: level = "high"
    elif score > 40: level = "medium"
    else: level = "low"
    return {"risk_score": score, "risk_level": level}
