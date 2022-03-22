from sqlalchemy import (Boolean, Column, ForeignKey, Integer, SmallInteger,
                        String, Table)
from sqlalchemy.orm import relationship

from .database import Base

tag_association_table = Table(
    "association",
    Base.metadata,
    Column("activity", ForeignKey("activities.id"), primary_key=True),
    Column("tag", ForeignKey("tags.id"), primary_key=True),
)


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)

    created_by_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    created_by = relationship("Student", back_populates="activities")

    approved_by_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)
    approved_by = relationship("Teacher", back_populates="activities")

    approve_status = Column(SmallInteger, default=0)

    title = Column(String(255), nullable=False)
    description = Column(String(2047), nullable=True)
    website = Column(String(511), nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="activities")

    tags = relationship(
        "Tag", secondary=tag_association_table, back_populates="activities"
    )

    score = Column(Integer, nullable=True)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    display_name = Column(String(31), nullable=False)

    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    salt = Column(String(31), nullable=False)

    grade = Column(SmallInteger, nullable=False)
    cls = Column(String(1), nullable=True)

    activities = relationship("Activity", back_populates="created_by")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

    email = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    salt = Column(String(63), nullable=False)

    activities = relationship("Activity", back_populates="approved_by")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(String(2047), nullable=False)

    activities = relationship("Activity", back_populates="category")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)
    description = Column(String(2047), nullable=False)

    activities = relationship(
        "Activity", secondary=tag_association_table, back_populates="tags"
    )
