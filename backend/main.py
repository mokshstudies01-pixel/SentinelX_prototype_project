from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load model and labels
model = joblib.load("model/threat_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

@app.get("/")
def home():
    return {"message": "AI Cyber Threat Detection API is running!"}

from backend.data_stream import get_next_row

@app.get("/predict")
def predict():

    # Get next real row
    sample_df = get_next_row()

    # Predict
    prediction = model.predict(sample_df)

    attack_name = label_encoder.inverse_transform(prediction)[0]

    return {
        "prediction": attack_name
    }
