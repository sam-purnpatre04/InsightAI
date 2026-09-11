from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.api.upload import router as upload_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload_router)


app.mount("/reports", StaticFiles(directory="reports"), name="reports")


@app.get("/")
def home():
    return {
        "project": "InsightAI",
        "status": "Running",
        "message": "Welcome to InsightAI 🚀"
    }