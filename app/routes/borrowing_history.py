from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import BorrowingHistory
from app.schemas import BorrowingHistoryResponse

router = APIRouter()


@router.get("/me", response_model=list[BorrowingHistoryResponse])
def get_my_borrowing_history(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    history = (
        db.query(BorrowingHistory).filter(BorrowingHistory.user_id == user["id"]).all()
    )
    if not history:
        raise HTTPException(status_code=404, detail="No borrowing history found")
    return history


@router.get("/", response_model=list[BorrowingHistoryResponse])
def get_all_borrowing_history(
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    if user["role"] not in ["Librarian", "Admin"]:
        raise HTTPException(
            status_code=403, detail="Access forbidden: Librarian or Admin role required"
        )
    history = db.query(BorrowingHistory).all()
    return history


@router.get("/{user_id}", response_model=list[BorrowingHistoryResponse])
def get_user_borrowing_history(
    user_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    if user["role"] not in ["Librarian", "Admin"]:
        raise HTTPException(
            status_code=403, detail="Access forbidden: Librarian or Admin role required"
        )
    history = (
        db.query(BorrowingHistory).filter(BorrowingHistory.user_id == user_id).all()
    )
    if not history:
        raise HTTPException(
            status_code=404, detail="No borrowing history found for this user"
        )
    return history
