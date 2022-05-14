import datetime
from typing import Optional

from pydantic import BaseModel, validator
from pydantic.main import ModelMetaclass


# metaclass making every class optional
class AllOptional(ModelMetaclass):
    def __new__(self, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith('__'):
                annotations[field] = Optional[annotations[field]]
        namespaces['__annotations__'] = annotations
        return super().__new__(self, name, bases, namespaces, **kwargs)


# Tag models
class TagBase(BaseModel):
    title: str
    description: Optional[str] = None


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    pass

    class Config:
        orm_mode = True

###############
# User models #
###############

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

class UserUpdate(UserBase, metaclass=AllOptional):
    pass

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
    status: int

    @validator("status")
    def allowed_status(cls, v):
        assert v in (-1, 0, 1), "Status must be in (-1, 0, 1), got {v}"
        return v
