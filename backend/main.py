from os import environ

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi_login import LoginManager
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

load_dotenv()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
manager = LoginManager(environ["LOGIN_SECRET"], "/login")



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Student methods
@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.get("/students/{student_id}/", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id=student_id)

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.get_student_by_email(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_student(db=db, student=student)

@app.delete("/students/{student_id}/", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete_student(db, student_id)
    



# Teacher methods
@app.get("/teachers/", response_model=list[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teachers(db, skip=skip, limit=limit)

@app.get("/teachers/{teacher_id}/", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return crud.get_teacher(db, teacher_id=teacher_id)

@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher_by_email(db, email=teacher.email)
    if db_teacher:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_teacher(db=db, teacher=teacher)

@app.delete("/teachers/{teacher_id}/", status_code=204)
def delete_student(teacher_id: int, db: Session = Depends(get_db)):
    crud.delete_teacher(db, teacher_id)



# Activity methods
@app.get("/activities/", response_model=list[schemas.Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_activities(db, skip=skip, limit=limit)

@app.get("/activities/{activity_id}/", response_model=schemas.Activity)
def read_activity(activity_id: int):
    return crud.get_activity(db, activity_id=activity_id)

@app.post("/activities/", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db, activity=activity)
