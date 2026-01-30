from fastapi import FastAPI, HTTPException
from config import APP_NAME, APP_VERSION, ENVIRONMENT
import random
import time

app = FastAPI(title=APP_NAME)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "environment": ENVIRONMENT,
        "version": APP_VERSION
    }

@app.get("/info")
def app_info():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    }

@app.get("/simulate-failure")
def simulate_failure():
    # Simulate random failure (used for testing resilience)
    if random.choice([True, False]):
        raise HTTPException(status_code=500, detail="Simulated application failure")
    return {"message": "Request succeeded"}

@app.get("/delay")
def simulate_delay():
    # Simulate slow response (used for load and timeout testing)
    time.sleep(3)
    return {"message": "Delayed response"}
