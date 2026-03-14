import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "student_performance_model.pkl")

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model