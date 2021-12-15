from pydantic import BaseModel, validator, HttpUrl
from typing import Optional


class Image(BaseModel):
    title: str
    url: HttpUrl


class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    # url: HttpUrl
    # name: types.constr(strip_whitespace=True, min_length=3)
    image: Optional[Image]

    @validator('title')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
