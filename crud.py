from ast import literal_eval
from sqlalchemy.orm import Session
import schemas
import models

## setup CRUD function
## Get all pollutions data
def get_pm(db: Session, skip= 0, limit= 100):
    return db.query(models.PMData).offset(skip).limit(limit).all()

def insert_data(db: Session, item: schemas.PMInsert):
    db_item = models.PMData(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item