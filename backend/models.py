from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Table,
    Date,
)
from sqlalchemy.orm import relationship

from database import Base


tag_association_table = Table(
    "association",
    Base.metadata,
    Column("activity", ForeignKey("activities.id"), primary_key=True),
    Column("tag", ForeignKey("tags.title"), primary_key=True),
)


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, nullable=False)

    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_by = relationship(
        "User", back_populates="created_activities", foreign_keys=[created_by_id]
    )

    reviewed_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    reviewed_by = relationship(
        "User", back_populates="reviewed_activities", foreign_keys=[reviewed_by_id]
    )

    review_status = Column(SmallInteger, default=0)

    title = Column(String(255), nullable=False)
    description = Column(String(2047), nullable=True)
    website = Column(String(511), nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="activities")

    tags = relationship(
        "Tag", secondary=tag_association_table, back_populates="activities"
    )

    score = Column(Integer, nullable=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    display_name = Column(String(31), nullable=True)

    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    salt = Column(String(31), nullable=False)

    grade = Column(SmallInteger, nullable=True)
    cls = Column(String(1), nullable=True)

    role = Column(Integer, nullable=False)

    created_activities = relationship(
        "Activity", back_populates="created_by", foreign_keys=[Activity.created_by_id]
    )
    reviewed_activities = relationship(
        "Activity", back_populates="reviewed_by", foreign_keys=[Activity.reviewed_by_id]
    )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)
    description = Column(String(2047), nullable=False)

    activities = relationship("Activity", back_populates="category")


class Tag(Base):
    __tablename__ = "tags"

    title = Column(String(255), primary_key=True, nullable=False)
    description = Column(String(2047), nullable=True)

    activities = relationship(
        "Activity", secondary=tag_association_table, back_populates="tags"
    )
