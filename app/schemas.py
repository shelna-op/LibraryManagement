# schemas
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    id: int
    email: str
    username: str
    role: str
    password_hash: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    role: str
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    id: int
    email: str
    username: str
    role: str
    password_hash: str


class BorrowingHistoryResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: datetime
    return_date: Optional[datetime] = None
    status: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    category: Optional[str]
    published_year: Optional[int]
    copies_available: int
    total_copies: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    category: Optional[str] = None
    published_year: Optional[int] = None
    copies_available: Optional[int] = None
    total_copies: Optional[int] = None


class BookResponse(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class BorrowRequest(BaseModel):
    book_id: int


class BorrowResponse(BaseModel):
    message: str
    book_id: int
    borrow_date: datetime


class ReturnRequest(BaseModel):
    book_id: int


class ReturnResponse(BaseModel):
    message: str
    book_id: int
    return_date: datetime
