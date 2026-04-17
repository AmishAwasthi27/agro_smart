from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI()

# -----------------------------
# Model will be loaded safely
# -----------------------------
model = None

@app.on_event("startup")
def load_model():
    global model
    model = pickle.load(open("crop_model.pkl", "rb"))


# -----------------------------
# Request body schema
# -----------------------------
class CropInput(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float


# -----------------------------
# Root endpoint (test API)
# -----------------------------
@app.get("/")
def home():
    return {"message": "Crop Recommendation API is running"}


# -----------------------------
# Prediction endpoint
# -----------------------------
@app.post("/predict")
def predict(data: CropInput):

    input_data = np.array([[
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])

    prediction = model.predict(input_data)[0]

    return {
        "recommended_crop": prediction
    }