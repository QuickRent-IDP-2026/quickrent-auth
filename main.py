from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

DATA_SERVICE_URL = os.getenv("DATA_SERVICE_URL", "http://data-service:8000")

@app.post("/register")
def register(user: dict):
    response = requests.post(f"{DATA_SERVICE_URL}/users", json=user)
    
    if response.status_code == 200:
        return {"message": "Registration successful", "data": response.json()}
    else:
        raise HTTPException(status_code=400, detail="Registration failed at Data Level")

@app.get("/health")
def health():
    return {"status": "Auth Service is healthy"}