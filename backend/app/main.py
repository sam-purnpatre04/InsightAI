from fastapi import FastAPI
from backend.app.api.upload import router as upload_router

app = FastAPI()

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "project": "InsightAI",
        "status": "Running",
        "message": "Welcome to InsightAI 🚀"
    }