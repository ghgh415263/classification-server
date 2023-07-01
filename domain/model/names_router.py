from database import SessionLocal
from fastapi import APIRouter

router = APIRouter(
    prefix="",
)

@router.get("/models")
def getModels():
    db = SessionLocal()
    models = db.query(Model).all()
    return models