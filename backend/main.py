import datetime
from datetime import timedelta
from os import environ

from dotenv import load_dotenv
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from pypbkdf2 import PyPBKDF2 as PasswordHasher

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
manager = LoginManager(
    environ["LOGIN_SECRET"], "/login", default_expiry=timedelta(hours=2)
)

origins = [
    *environ["DEV_FRONTEND_URL"].split(","),
    environ["PROD_FRONTEND_URL"],
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.expunge_all()
    finally:
        db.close()


# User query
@manager.user_loader()
def query_user(user_email: str, db: Session = Depends(get_db)):
    db = SessionLocal()
    return crud.get_user_by_email(db, user_email)


# Login method
@app.post("/login/")
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    email = data.username
    password = data.password

    user = crud.get_user_by_email(db, email)
    if not user:
        raise InvalidCredentialsException
    p = PasswordHasher(salt_size=63)
    if not p.verify_password(password, user.password_hash, user.salt):
        raise InvalidCredentialsException
    scopes = []
    if user.role >= 1:
        scopes.append("teacher")
    if user.role >= 2:
        scopes.append("admin")
    access_token = manager.create_access_token(data={"sub": email}, scopes=scopes)
    return {"access_token": access_token}


# Register method
@app.post("/register/")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    if user.role != 0:
        if not user.register_token:
            raise HTTPException(
                status_code=400,
                detail="Tried to register as a teacher, yet no token given",
            )
        if user.register_token != environ["REGISTER_TEACHER_SECRET"]:
            raise HTTPException(status_code=400, detail="Wrong teacher token")
    del user.register_token
    return crud.create_user(db=db, user=user)


# Get info about authenticated user
@app.get("/user/me/", response_model=schemas.User)
def read_authenticated_user(user=Depends(manager)):
    return user


###################
# Student methods #
###################

# Read own activities
@app.get("/student/activities/", response_model=list[schemas.Activity])
def student_get_activities(user=Depends(manager), db: Session = Depends(get_db)):
    return user.created_activities


# Create activity
@app.post("/student/activities/", response_model=schemas.Activity)
def student_create_activity(
    activity: schemas.ActivityCreate,
    user=Depends(manager),
    db: Session = Depends(get_db),
):
    activity = activity.dict()
    activity["created_by_id"] = user.id
    year, month, day = [int(i) for i in activity["date"].split("-")]
    activity["date"] = datetime.date(year, month, day)
    for index, tag in enumerate(activity["tags"]):
        db_tag = db.query(models.Tag).filter(models.Tag.title == tag).first()
        if not db_tag:
            db_tag = crud.create_tag(db, tag=schemas.TagCreate(title=tag))
        activity["tags"][index] = db_tag

    new_activity = models.Activity(**activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity


###################
# Teacher methods #
###################

# Read all activities
@app.get("/teacher/activities/", response_model=list[schemas.Activity])
def read_activities(
    user=Security(manager, scopes=["teacher"]),
    db: Session = Depends(get_db),
):
    return crud.get_activities(db)


@app.get("/teacher/students/", response_model=list[schemas.User])
def read_students(
    user=Security(manager, scopes=["teacher"]), db: Session = Depends(get_db)
):
    return (
        db.query(models.User)
        .filter(models.User.role == 0)
        .order_by(models.User.cls, models.User.grade, models.User.last_name)
        .all()
    )


# Review an activity and either accept or reject it.
@app.post("/teacher/review/", response_model=schemas.Activity)
def review_activity(review: schemas.ActivityReview, db: Session = Depends(get_db)):
    query = db.query(models.Activity).filter(models.Activity.id == review.activity_id)
    activity = query.first()
    if not activity:
        raise HTTPException(status_code=400, detail="Activity not found.")

    query.update(
        {
            "reviewed_by_id": review.teacher_id if review.status else None,
            "review_status": review.status,
        }
    )
    db.commit()
    db.refresh(activity)
    return activity


# User CRUD methods
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}/", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id=user_id)


@app.delete("/users/{user_id}/", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    crud.delete_user(db, user_id)


@app.get("/activities/{activity_id}/", response_model=schemas.Activity)
def read_activity(activity_id: int):
    return crud.get_activity(db, activity_id=activity_id)


# Category CRUD methods
@app.get("/categories/", response_model=list[schemas.Category])
def read_categories(
    skip: int = 0,
    limit: int = 100,
    user=Depends(manager),
    db: Session = Depends(get_db),
):
    return crud.get_categories(db, skip=skip, limit=limit)


@app.get("/categories/{category_id}/", response_model=schemas.Category)
def read_category(category_id: int):
    return crud.get_category(db, category_id=category_id)


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category=category)


# Tag CRUD methods
@app.get("/tags/", response_model=list[schemas.Tag])
def read_tags(
    skip: int = 0,
    limit: int = 100,
    user=Depends(manager),
    db: Session = Depends(get_db),
):
    return crud.get_tags(db, skip=skip, limit=limit)


@app.get("/tags/{tag_id}/", response_model=schemas.Tag)
def read_tag(tag_id: int):
    return crud.get_tag(db, category_id=category_id)


@app.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db, tag=tag)
