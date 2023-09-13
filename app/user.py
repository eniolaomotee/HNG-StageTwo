from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException, status, APIRouter,Response
from .database import get_db

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_person(payload: schemas.PersonBaseSchema, db: Session = Depends(get_db)):
    new_person = models.Person(**payload.dict())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return {"status": "success", "person": new_person}


@router.patch('/{user_id}')
def update_person(user_id: str, payload: schemas.PersonBaseSchema, db: Session = Depends(get_db)):
    person_query = db.query(models.Person).filter(models.Person.id == user_id)
    db_person = person_query.first()

    if not db_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No note with this id: {user_id} found')
    update_data = payload.dict(exclude_unset=True)
    person_query.filter(models.Person.id == user_id).update(update_data,
                                                       synchronize_session=False)
    db.commit()
    db.refresh(db_person)
    return {"status": "success", "person": db_person}


@router.get('/{user_id}')
def get_person(user_id: str, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == user_id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No person with this id: {user_id} found")
    return {"status": "success", "Person": person}

@router.delete('/{user_id}')
def delete_person(user_id: str, db: Session = Depends(get_db)):
    person_query = db.query(models.Person).filter(models.Person.id == user_id)
    person = person_query.first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No person with this id: {user_id} found')
    person_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)