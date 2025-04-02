 Library Management System API

📌 Overview

This is a FastAPI-based Library Management System that provides functionalities for managing books, users, borrowing, and returning books. The API is secured using JWT authentication.
📌 Features

📖 Manage Books (Add, Update, Delete, Search)

👤 User Authentication (JWT-based authentication)

📚 Borrowing & Returning Books

🛡 Role-based Access Control (Librarians & Users)

📊 Swagger UI for API Testing

📌 Prerequisites

Before setting up the project, ensure you have the following installed:

Python 3.8+

MySQL Server (8.0 recommended)

pip (Python package manager)

Virtual Environment (optional but recommended)

Database Setup (MySQL)

Install MySQL (if not installed)

Windows: Download from [MySQL official site](https://dev.mysql.com/downloads/installer/)

macOS: Install via Homebrew:

brew install mysql

Linux: Install via APT (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install mysql-server
```

Start MySQL Service
```bash
sudo systemctl start mysql  # For Linux
brew services start mysql   # For macOS
```

Create Database & User

eg:
```sql
CREATE DATABASE LibraryManagementDB;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Admin123!';
GRANT ALL PRIVILEGES ON LibraryManagementDB.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
```

🛠 Installation & Setup

1️⃣ Clone the Repository

```bash
git clone https://github.com/shelna-op/LibraryManagement.git
cd LibraryManagement 
```

2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file and add:
```bash
DATABASE_URL = "mysql+pymysql://username:password@localhost/LibrarymanagementDB"
SECRET_KEY = "your-secret-key"
SECRET_KEY_ALGORITHM = "HS256"
```

You can generate SECRET_KEY as follows:
python script
-------------
```bash
import secrets
print(secrets.token_hex(32))
```

You can use python add_sample_data.py to add some sample data in the DB

6️⃣ Start the FastAPI Server

uvicorn main:app --reload

The server will run at http://127.0.0.1:8000.

🔑 Authentication

This API uses JWT-based authentication.

Register a new user: POST /users/register

Keep the access token received while registering the user

Use the token for API calls by adding it to the Authorization header:

Authorization: Bearer YOUR_ACCESS_TOKEN

📘 API Documentation

After running the server, you can access the API documentation at:

Swagger UI: http://127.0.0.1:8000/docs


🏗 Project Structure
```bash
.
├── app/
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas
│   ├── routes/
│   │   ├── books.py        # Book-related endpoints
│   │   ├── users.py        # User authentication
│   │   ├── borrowing.py    # Borrowing logic
│   │   ├── borrowing_history.py  # Borrowing history
│   ├── auth.py             # Authentication & JWT logic
│   ├── database.py         # Database connection
│
├── main.py                 # FastAPI app initialization
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables

```

