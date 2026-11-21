import os
from fastapi import FastAPI, Query, HTTPException
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
SECRET_KEY = os.getenv("SECRET_KEY")

@app.get("/")
def home():
    return {
        "message": "Welcome to my First FastAPI Application!!"
    }

# endpoint = http://127.0.0.1:8000/verify?key=my-secret-key
@app.get("/verify")
def verify(key: str = Query(...)):
    if not SECRET_KEY:
        raise HTTPException(
            status_code = 500,
            detail = "Server secret key is not configured"
        )
    if key==SECRET_KEY:
        return{
            "message": "Authentication successful"
        }
    raise HTTPException(
        status_code=401,
        detail = "Invalid secret key"
    )

@app.get("/health")
def health():
    return{
        "status": "healthy",
        "message":"Application is running successfully"
    }
