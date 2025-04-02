import os

from dotenv import load_dotenv
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.logger import logger

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("SECRET_KEY_ALGORITHM")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def generate_user_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Security(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logger.info(payload)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def librarian_required(user: dict):
    if user["role"] != "Librarian":
        raise HTTPException(status_code=403, detail="Access forbidden")
