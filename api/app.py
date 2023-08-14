import uvicorn
from fastapi import FastAPI, UploadFile, File
import json
import joblib
import numpy as np
import pandas as pd

# Create the app object
app = FastAPI()

# Load the saved model
model = joblib.load("/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/api/model.pkl")

# Define the routes
@app.get('/')
def index():
    return {'message': 'Hello, Everyone!'}

@app.get('/Welcome/{name}')
def get_name(name: str):
    return {'Welcome to my ML model': name}

@app.post('/predict_csv')
def predict_loan_csv(file: UploadFile = File(...)):
    # Read the CSV file
    df = pd.read_csv(file.file)

    # Make predictions for each row
    predictions = []
    for _, row in df.iterrows():
        input_data = np.array([row.values])
        prediction = model.predict(input_data)
        if prediction == 0:
            ispu = "BAIK"
        if prediction == 1:
            ispu="SEDANG"
        else:
            ispu = "TIDAK SEHAT"
        predictions.append(ispu)

    return {"predictions": predictions}

if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8080)
