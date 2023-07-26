from fastapi import FastAPI, Depends
import models, crud, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

## Main API code
models.Base.metadata.create_all(bind= engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"msg": "Hello"}

    ## GET all Pollutions data
@app.get("/pollutions/", response_model= list[schemas.PMResponse])
def read_pm(skip= 0, limit= 100, db: Session = Depends(get_db)):
    pmdata = crud.get_pm(db, skip= skip, limit= limit)
    return pmdata

@app.post("/pollutions/", response_model= schemas.PMInsert)
def insert_pm_data(item: schemas.PMInsert, db: Session = Depends(get_db)):
    return crud.insert_data(db=db, item= item)