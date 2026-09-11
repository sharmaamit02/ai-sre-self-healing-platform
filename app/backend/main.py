from fastapi import FastAPI, HTTPException
import time
import os

app = FastAPI(
    title="SentinelOps Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "service": "sentinelops-backend",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/ready")
def ready():
    return {
        "status": "ready"
    }


@app.get("/api/status")
def status():
    return {
        "application": "SentinelOps AI",
        "service": "backend",
        "environment": os.getenv("ENVIRONMENT", "dev"),
        "status": "operational"
    }


@app.get("/api/fail")
def fail():
    raise HTTPException(
        status_code=500,
        detail="Simulated application failure"
    )


@app.get("/api/slow")
def slow():
    time.sleep(5)

    return {
        "status": "completed",
        "message": "Simulated slow API response"
    }
