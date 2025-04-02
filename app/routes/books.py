from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.auth import get_current_user, librarian_required
from app.database import get_db
from app.models import Book
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter()


@router.get("/search", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None, description="Search by book title"),
    author: Optional[str] = Query(None, description="Search by author name"),
    category: Optional[str] = Query(None, description="Search by category"),
    isbn: Optional[str] = Query(None, description="Search by ISBN"),
    published_year: Optional[int] = Query(None, description="Search by published year"),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if category:
        query = query.filter(Book.category.ilike(f"%{category}%"))
    if isbn:
        query = query.filter(Book.isbn == isbn)
    if published_year:
        query = query.filter(Book.published_year == published_year)

    books = query.all()
    return books


@router.get("/", response_model=List[BookResponse])
def list_books(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    books = db.query(Book).all()
    return books


@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return existing_book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def add_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    librarian_required(user)
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book: BookUpdate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    librarian_required(user)
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict(exclude_unset=True).items():
        setattr(existing_book, key, value)
    db.commit()
    db.refresh(existing_book)
    return existing_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    librarian_required(user)
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(existing_book)
    db.commit()
    return {"message": "Book deleted successfully"}
