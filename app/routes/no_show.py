from fastapi import APIRouter, Body
import joblib
import numpy as np

router = APIRouter(prefix='/no-show', tags=["NoShowPrediction"])
model = joblib.load('models/no_show_model.pkl')

@router.post('/predict')
def predict(data: dict = Body(...)):
    # Example: data = {"age": 34, "past_no_shows": 2, "weekday": 3, ...}
    X = np.array([data[k] for k in sorted(data.keys())]).reshape(1, -1)
    prob = model.predict_proba(X)[0,1]
    return {"no_show_probability": round(float(prob), 3)}
