from database import SessionLocal
from fastapi import APIRouter

from models import AnalysisModel

router = APIRouter(
    prefix="",
)

@router.get("/models")
def getModels():
    db = SessionLocal()
    models = db.query(AnalysisModel).all()

    print(models)
    return models

