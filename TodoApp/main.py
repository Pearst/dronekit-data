from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close


@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)])