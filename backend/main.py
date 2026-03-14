from fastapi import FastAPI
import numpy as np
from model_loader import load_model
from schemas import StudentData

app = FastAPI()

model = load_model()

@app.get("/")
def home():
    return {"message": "Student Performance Prediction API"}

@app.post("/predict")

def predict(data: StudentData):

    features = np.array([[
        data.hours_studied,
        data.previous_scores,
        data.extracurricular_activities,
        data.sleep_hours,
        data.sample_papers_practiced
    ]])

    prediction = model.predict(features)

    return {
        "Predicted Performance Index": round(float(prediction[0]),2)
    }