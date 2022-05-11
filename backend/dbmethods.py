import crud
import schemas
import models
import datetime

from sqlalchemy.orm import Session

def create_activity(activity: schemas.ActivityCreate, user_id, db: Session, teacher=False, teacher_id=None):
    activity = activity.dict()
    activity["created_by_id"] = user_id
    year, month, day = [int(i) for i in activity["date"].split("-")]
    activity["date"] = datetime.date(year, month, day)
    for index, tag in enumerate(activity["tags"]):
        db_tag = db.query(models.Tag).filter(models.Tag.title == tag).first()
        if not db_tag:
            db_tag = crud.create_tag(db, tag=schemas.TagCreate(title=tag))
        activity["tags"][index] = db_tag

    if teacher and teacher_id:
        activity["reviewed_by_id"] = teacher_id
        activity["review_status"] = 1

    new_activity = models.Activity(**activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity

