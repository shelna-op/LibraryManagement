from passlib.hash import bcrypt
from app.database import SessionLocal
from app.models import Book, User, BorrowingHistory
from datetime import datetime

# Create a database session
db = SessionLocal()

try:
    # Add sample books
    books = [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            isbn="9780743273565",
            category="Fiction",
            published_year=1925,
            copies_available=5,
            total_copies=5,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        Book(
            title="1984",
            author="George Orwell",
            isbn="9780451524935",
            category="Dystopian",
            published_year=1949,
            copies_available=3,
            total_copies=3,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        Book(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            isbn="9780061120084",
            category="Fiction",
            published_year=1960,
            copies_available=4,
            total_copies=4,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        Book(
            title="Pride and Prejudice",
            author="Jane Austen",
            isbn="9780141439518",
            category="Romance",
            published_year=1813,
            copies_available=2,
            total_copies=2,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        Book(
            title="The Catcher in the Rye",
            author="J.D. Salinger",
            isbn="9780316769488",
            category="Fiction",
            published_year=1951,
            copies_available=3,
            total_copies=3,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
    ]
    db.add_all(books)

    # Add sample users
    users = [
        User(
            username="john_doe",
            password_hash=bcrypt.hash("password123"),  # Hash the password
            email="john@example.com",
            role="User",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        User(
            username="admin_user",
            password_hash=bcrypt.hash("adminpassword"),  # Hash the password
            email="admin@example.com",
            role="Librarian",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
        User(
            username="jane_doe",
            password_hash=bcrypt.hash("securepass"),  # Hash the password
            email="jane@example.com",
            role="User",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        ),
    ]

    db.add_all(users)

    # Commit the books and users first to ensure their IDs are available
    db.commit()

    # Add sample borrowing history
    borrowing_history = [
        BorrowingHistory(
            user_id=1,  # Assuming user with ID 1 exists
            book_id=1,  # Assuming book with ID 1 exists
            borrow_date=datetime(2023, 3, 1, 10, 0, 0),
            return_date=None,  # Book not yet returned
            status="Borrowed",
        ),
        BorrowingHistory(
            user_id=1,  # Assuming user with ID 1 exists
            book_id=2,  # Assuming book with ID 2 exists
            borrow_date=datetime(2023, 2, 15, 14, 30, 0),
            return_date=datetime(2023, 3, 5, 16, 0, 0),  # Book returned
            status="Returned",
        ),
        BorrowingHistory(
            user_id=2,  # Assuming user with ID 2 exists
            book_id=3,  # Assuming book with ID 3 exists
            borrow_date=datetime(2023, 3, 10, 9, 0, 0),
            return_date=None,  # Book not yet returned
            status="Borrowed",
        ),
    ]
    db.add_all(borrowing_history)

    # Commit all changes
    db.commit()
    print("Sample data added successfully!")

except Exception as e:
    print(f"Error adding sample data: {e}")
    db.rollback()
finally:
    db.close()
