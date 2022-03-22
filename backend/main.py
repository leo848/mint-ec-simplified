from os import environ

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi_login import LoginManager
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# manager = LoginManager(environ["LOGIN_SECRET"], "/login")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# User CRUD methods
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}/", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    if user.role != 0:
        if not user.register_token:
            raise HTTPException(status_code=400, detail="Tried to register as a teacher, yet no token given")
        if user.register_token != environ["REGISTER_TEACHER_SECRET"]:
            raise HTTPException(status_code=400, detail="Wrong teacher token")
    del user.register_token
    return crud.create_user(db=db, user=user)


@app.delete("/users/{user_id}/", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)



# Activity CRUD methods
@app.get("/activities/", response_model=list[schemas.Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_activities(db, skip=skip, limit=limit)


@app.get("/activities/{activity_id}/", response_model=schemas.Activity)
def read_activity(activity_id: int):
    return crud.get_activity(db, activity_id=activity_id)


@app.post("/activities/", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db, activity=activity)


# Category CRUD methods
@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip=skip, limit=limit)


@app.get("/categories/{category_id}/", response_model=schemas.Category)
def read_category(category_id: int):
    return crud.get_category(db, category_id=category_id)


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category=category)


# (As a teacher) review an activity and either accept or reject it.
@app.post("/review_activity", response_model=schemas.Activity)
def review_activity(review: schemas.ActivityReview, db: Session = Depends(get_db)):
    query = db.query(models.Activity).filter(models.Activity.id == review.activity_id)
    activity = query.first()
    if not activity:
        raise HTTPException(status_code=400, detail="Activity not found.")

    query.update(
        {
            "reviewed_by_id": review.teacher_id if review.status else None,
            "reviewed_status": review.status,
        }
    )
    db.commit()
    db.refresh(activity)
    return activity
