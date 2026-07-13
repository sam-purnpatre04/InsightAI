from fastapi import APIRouter, UploadFile, File

from backend.app.services.csv_service import read_csv

router = APIRouter()


@router.post("/upload")
def upload_csv(file: UploadFile = File(...)):
   return read_csv(file)