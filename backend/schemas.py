from typing import Optional
import datetime

from pydantic import BaseModel, validator

# Tag models
class TagBase(BaseModel):
    title: str
    description: Optional[str] = None


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    # activities: list[Activity] = [] # cross-referential problem, no solution yet FIXME

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

    role: Optional[int] = 0


class UserCreate(UserBase):
    password: str
    register_token: Optional[str] = None


class User(UserBase):
    id: int

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

    class Config:
        orm_mode = True

# Activity models
class ActivityBase(BaseModel):
    title: str
    description: Optional[str] = None
    website: Optional[str] = None

    category_id: int


class ActivityCreate(ActivityBase):
    tags: list[str] = []
    date: str

class ActivityDBCreate(ActivityBase):
    tags: list[Tag] = []
    date: datetime.date
    # created_by_id: int
    created_by: User



class Activity(ActivityDBCreate):
    id: int

    category: Category
    # reviewed_by_id: Optional[int] = None
    reviewed_by: Optional[User] = None
    review_status: int = 0

    score: Optional[int] = None

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
