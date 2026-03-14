import streamlit as st
import requests
import os

st.title("🎓 Student Performance Predictor")

API_URL = os.getenv("API_URL", "http://localhost:8000")

hours = st.slider("Hours Studied", 0, 12, 5)
previous_scores = st.slider("Previous Scores", 0, 100, 50)

activity = st.selectbox("Extracurricular Activities", ["No","Yes"])

sleep = st.slider("Sleep Hours", 4, 10, 7)
papers = st.slider("Sample Papers Practiced", 0, 10, 3)

activity = 1 if activity=="Yes" else 0

if st.button("Predict"):

    payload = {
        "hours_studied":hours,
        "previous_scores":previous_scores,
        "extracurricular_activities":activity,
        "sleep_hours":sleep,
        "sample_papers_practiced":papers
    }

    response = requests.post(
        f"{API_URL}/predict",
        json=payload
    )

    result = response.json()

    st.success(result["Predicted Performance Index"])