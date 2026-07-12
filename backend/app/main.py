from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {
        "project": "InsightAI",
        "status": "Running",
        "message": "Welcome to InsightAI 🚀"
    }