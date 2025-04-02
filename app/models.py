from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

import enum

from datetime import datetime


Base = declarative_base()


class Role(enum.Enum):
    User = "User"

    Librarian = "Librarian"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    category = Column(String(100))
    published_year = Column(Integer)
    copies_available = Column(Integer, default=0)
    total_copies = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    borrowed_by = relationship(
        "BorrowingHistory", back_populates="book", cascade="all, delete"
    )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(50), default="User")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    borrowed_books = relationship(
        "BorrowingHistory", back_populates="user", cascade="all, delete"
    )


class BorrowingHistory(Base):
    __tablename__ = "borrowing_history"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    book_id = Column(
        Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False
    )
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)
    status = Column(String(50), default="Borrowed")
    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book", back_populates="borrowed_by")
