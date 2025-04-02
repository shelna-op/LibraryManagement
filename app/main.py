from fastapi import FastAPI

from app.database import init_db
from app.routes import books, borrowing, borrowing_history
from app.routes.users import router as users_router

app = FastAPI()

init_db()

app.include_router(books.router, prefix="/books", tags=["Books"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API!"}


app.include_router(borrowing.router, prefix="/borrowing", tags=["Borrowing"])
app.include_router(
    borrowing_history.router, prefix="/borrowing-history", tags=["Borrowing History"]
)
app.include_router(users_router)
