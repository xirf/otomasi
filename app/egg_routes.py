from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from . import db, models

router = APIRouter()

@router.post("/bad")
def increment_bad_egg(db: Session = Depends(db.get_db)):
    try:
        today = date.today().isoformat()
        item = db.query(models.Item).filter(models.Item.date == today).first()
        if item:
            item.bad_count += 1
        else:
            item = models.Item(bad_count=1, good_count=0, date=today)
            db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/good")
def increment_good_egg(db: Session = Depends(db.get_db)):
    try:
        today = date.today().isoformat()
        item = db.query(models.Item).filter(models.Item.date == today).first()
        if item:
            item.good_count += 1
        else:
            item = models.Item(bad_count=0, good_count=1, date=today)
            db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
