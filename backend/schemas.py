from typing import Optional

from pydantic import BaseModel, validator

# Tag models
class TagBase(BaseModel):
    title: str
    description: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int
    # activities: list[Activity] = [] # cross-referential problem, no solution yet FIXME

    class Config:
        orm_mode = True


# Activity models
class ActivityBase(BaseModel):
    title: str
    description: Optional[str] = None
    website: Optional[str] = None

    created_by_id: int

    category_id: int

    tags: list[Tag] = []


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    approved_by_id: Optional[int] = None
    approve_status: int = 0

    score: Optional[int] = None

    class Config:
        orm_mode = True


# Student models
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    display_name: str

    email: str

    grade: int
    cls: Optional[str] = None


class StudentCreate(StudentBase):
    password: str


class Student(StudentBase):
    id: int
    activities: list[Activity]

    class Config:
        orm_mode = True


# Teacher models
class TeacherBase(BaseModel):
    first_name: str
    last_name: str

    email: str


class TeacherCreate(TeacherBase):
    password: str


class Teacher(TeacherBase):
    id: int
    activities: list[Activity] = []

    class Config:
        orm_mode = True


# Category models
class CategoryBase(BaseModel):
    title: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    activities: list[Activity] = []

    class Config:
        orm_mode = True


# Other models
class ActivityReview(BaseModel):
    teacher_id: int
    activity_id: int
    approve_status: int

    @validator("approve_status")
    def allowed_status(cls, v):
        assert v in (-1, 0, 1), "Status must be in (-1, 0, 1), got {v}"
        return v
