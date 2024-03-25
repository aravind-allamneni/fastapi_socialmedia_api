from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class User(BaseModel):
    email: EmailStr


class UserIn(User):
    password: str


class UserLogin(User):
    password: str


class UserOut(User):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class PostIn(Post):
    pass


class PostExt(Post):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: PostExt
    votes: int

    class Config:
        from_attributes = True


class VoteIn(BaseModel):
    post_id: int
    vote_dir: Annotated[int, conint(le=1)]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
