from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book, BorrowingHistory
from app.schemas import BorrowRequest, BorrowResponse
from app.schemas import ReturnRequest, ReturnResponse
from app.auth import get_current_user
from datetime import datetime
from app.logger import logger

router = APIRouter()


@router.post("/borrow", response_model=BorrowResponse)
def borrow_book(
    borrow_request: BorrowRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    book = db.query(Book).filter(Book.id == borrow_request.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.copies_available <= 0:
        raise HTTPException(status_code=400, detail="No copies available for borrowing")

    borrowing = BorrowingHistory(
        user_id=user["id"],
        book_id=borrow_request.book_id,
        status="Borrowed",
    )
    book.copies_available -= 1
    db.commit()
    db.refresh(borrowing)

    return {
        "message": "Book borrowed successfully",
        "book_id": borrowing.book_id,
        "borrow_date": borrowing.borrow_date,
    }


@router.post("/return", response_model=ReturnResponse)
def return_book(
    return_request: ReturnRequest,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    logger.info("Return requested")
    borrowing = (
        db.query(BorrowingHistory)
        .filter(
            BorrowingHistory.book_id == return_request.book_id,
            BorrowingHistory.user_id == user["id"],
            BorrowingHistory.status == "Borrowed",
        )
        .first()
    )
    if not borrowing:
        raise HTTPException(
            status_code=404, detail="No active borrowing record found for this book"
        )

    borrowing.status = "Returned"
    borrowing.return_date = datetime.utcnow()

    book = db.query(Book).filter(Book.id == return_request.book_id).first()
    if book:
        book.copies_available += 1
    db.commit()
    return {"message": "Book returned successfully",
            "book_id": return_request.book_id,
            "return_date": borrowing.return_date
            }
