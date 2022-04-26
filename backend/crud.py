from pypbkdf2 import PyPBKDF2 as PasswordHasher
from sqlalchemy.orm import Session

import models, schemas



# User methods
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hasher = PasswordHasher(salt_size=63)
    password_hash, salt = hasher.hash_password(user.password)

    user_dict = user.dict()
    del user_dict["password"]

    new_db_user = models.User(
        **user_dict,
        password_hash=password_hash,
        salt=salt,
    )

    db.add(new_db_user)
    db.commit()
    db.refresh(new_db_user)
    return new_db_user

def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()



# Activity methods

def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def get_activities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Activity).offset(skip).limit(limit).all()


def create_activity(db: Session, activity: schemas.ActivityDBCreate):
    new_activity = models.Activity(**activity.dict())
    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)
    return new_activity


# Category methods

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category



# Tag methods

def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Category.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int=100):
    return db.query(models.Tag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: schemas.TagCreate):
    new_tag = models.Tag(**tag.dict())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag
