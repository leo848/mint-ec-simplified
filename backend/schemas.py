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
class ActivityStudentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    website: Optional[str] = None

    category_id: int

    tags: list[Tag] = []

class ActivityBase(ActivityStudentCreate):
    created_by_id: int


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    reviewed_by_id: Optional[int] = None
    review_status: int = 0

    score: Optional[int] = None

    class Config:
        orm_mode = True


# User models
class UserBase(BaseModel):
    first_name: str
    last_name: str
    display_name: Optional[str] = None

    email: str

    grade: Optional[int] = None
    cls: Optional[str] = None

    role: int = 0


class UserCreate(UserBase):
    password: str
    register_token: Optional[str] = None


class User(UserBase):
    id: int
    created_activities: Optional[list[Activity]] = None
    reviewed_activities: Optional[list[Activity]] = None


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
    status: int

    @validator("status")
    def allowed_status(cls, v):
        assert v in (-1, 0, 1), "Status must be in (-1, 0, 1), got {v}"
        return v
