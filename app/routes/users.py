from passlib.hash import bcrypt
from fastapi import APIRouter, Depends, HTTPException, logger
import sqlalchemy
from sqlalchemy.orm import Session
from app.auth import generate_user_access_token
from app.models import User
from app.database import get_db
from app.schemas import UserCreate, UserResponse

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    try:
        new_user = User(
            id=user.id,
            username=user.username,
            email=user.email,
            password_hash=bcrypt.hash(user.password_hash),
            role=user.role
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        token_data = {"username": new_user.username,
                      "id": new_user.id,
                      "role": new_user.role}
        user_token = generate_user_access_token(data=token_data)

    except sqlalchemy.exc.IntegrityError as e:
        logger.warn(e)
        raise HTTPException(status_code=400, detail="User data already exists")

    return {
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role,
        "access_token": user_token,
        "token_type": "bearer"
    }
