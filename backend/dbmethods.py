import crud
import schemas

from sqlalchemy.orm import Session

def create_activity(activity: schemas.ActivityCreate, user_id, db: Session):
    activity = activity.dict()
    activity["created_by_id"] = user_id
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

