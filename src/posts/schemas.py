from pydantic import BaseModel

"""
Schemas for Posts module

- PostCreate: Schema for creating a new post (request body)
- PostOut: Schema for returning post data (response body)

Pydantic BaseModel:
- Provides data validation
- Handles parsing of incoming JSON
- Serializes response to JSON automatically

orm_mode = True:
- Allows Pydantic models to read data from ORM (SQLAlchemy) objects
- Enables returning SQLAlchemy objects directly from endpoints
  without manually converting them to dicts
"""

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int
    is_active: bool

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    is_active: bool

    class Config:
        orm_mode = True
