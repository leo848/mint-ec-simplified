from pypbkdf2 import PyPBKDF2 as PasswordHasher
from sqlalchemy.orm import Session

from . import models, schemas


# General query method
def get_query(db: Session, model: type(models.Base), model_id: int):
    return db.query(model).filter(model.id == id)

# Student methods
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()


def create_student(db: Session, student: schemas.StudentCreate):
    hasher = PasswordHasher(salt_size=63)
    password_hash, salt = hasher.hash_password(student.password)

    student_dict = student.dict()
    del student_dict["password"]

    new_db_student = models.Student(
        **student_dict,
        password_hash=password_hash,
        salt=salt,
    )

    db.add(new_db_student)
    db.commit()
    db.refresh(new_db_student)
    return new_db_student

def delete_student(db: Session, student_id: int):
    db.query(models.Student).filter(models.Student.id == student_id).delete()
    db.commit()



# Teacher methods
def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()


def get_teacher_by_email(db: Session, email: str):
    return db.query(models.Teacher).filter(models.Teacher.email == email).first()


def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    hasher = PasswordHasher(salt_size=63)
    password_hash, salt = hasher.hash_password(teacher.password)

    teacher_dict = teacher.dict()
    del teacher_dict["password"]

    new_db_teacher = models.Teacher(
        **teacher_dict,
        password_hash=password_hash,
        salt=salt,
    )

    db.add(new_db_teacher)
    db.commit()
    db.refresh(new_db_teacher)
    return new_db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db.query(models.Teacher).filter(models.Teacher.id == teacher_id).delete()
    db.commit()


# Activity methods

def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activity).offset(skip).limit(limit).all()


def create_activity(db: Session, activity: schemas.ActivityCreate):
    new_activity = models.Activity(**activity.dict())
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity


# Category methods

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activity).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
