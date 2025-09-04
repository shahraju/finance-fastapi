from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Finance Advisor - Stock Close Predictor")

# model & features
MODEL_PATH = "best_gb_model.pkl"
FEATURES = ["open", "high", "low", "volume"]

# load once at startup
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Failed to load model: {e}")

class InputRow(BaseModel):
    open: float
    high: float
    low: float
    volume: float

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Finance Advisor API is live.",
        "docs": "/docs",
        "predict_endpoint": "/predict"
    }

@app.post("/predict")
def predict(item: InputRow):
    if model is None:
        raise HTTPException(status_code=500, detail="Model failed to load on server.")

    data = pd.DataFrame([{
        "open": item.open,
        "high": item.high,
        "low": item.low,
        "volume": item.volume
    }], columns=FEATURES)

    try:
        pred = model.predict(data)[0]
        return {"prediction": float(pred)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")
