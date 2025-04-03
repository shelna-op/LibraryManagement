 Library Management System API

📌 Overview

This is a FastAPI-based Library Management System that provides functionalities for managing books, users, borrowing, and returning books. The API is secured using JWT authentication.
📌 Features

📖 Manage Books (Add, Update, Delete, Search)

👤 User Authentication (JWT-based authentication)

📚 Borrowing & Returning Books

🛡 Role-based Access Control (Librarians & Users)

📊 Swagger UI for API Testing


🛠️ Project Structure

📂 LibraryManagement
├── 📂 app
│   ├── 📄 main.py             # FastAPI entry point
│   ├── 📄 database.py         # Database connection setup
│   ├── 📄 models.py           # Database models  # Database models
│   ├── 📄 schemas.py          # Pydantic schemas
│   ├── 📄 auth.py 
│   ├── 📂 routes              # API routes
│   │   ├── 📄 books.py        # Book-related endpoints
│   │   ├── 📄 users.py        # User authentication
│   │   ├── 📄 borrowing.py    # Borrowing logic
│   │   ├── 📄 borrowing_history.py  # Borrowing history
├── 📄 requirements.txt         # Python dependencies
├── 📄 Dockerfile               # Docker build file
├── 📄 docker-compose.yml       # Docker Compose config
├── 📄 .env                     # Environment variables
└── 📄 README.md                # Documentation


You need to generate SECRET_KEY:

using python script

```bash
import secrets
print(secrets.token_hex(32))
```

📘 FastAPI + MySQL Docker Setup 
-----------------------------------------------------------------------------------------------

📌 Prerequisites
Docker is installed

1️⃣ Clone the Repository

```bash
git clone https://github.com/shelna-op/LibraryManagement.git
cd LibraryManagement 
```
2️⃣ Create a .env File

Create a .env file in the project root and add the following environment variables:

Example:
```bash
MYSQL_ROOT_PASSWORD=Mysql123!
MYSQL_DATABASE=LibrarymanagementDB
MYSQL_USER=root
MYSQL_PASSWORD=Mysql123!
SECRET_KEY=<generated secret key>
DATABASE_URL="mysql+pymysql://root:Mysql123!@db:3306/LibrarymanagementDB"
```

3️⃣  Running with Docker Compose
```bash
docker-compose up -d
```

4️⃣ Access the FastAPI App

Go to: http://localhost:8000/docs

This will open the interactive API documentation (Swagger UI).


-----------------------------------------------------------------------------------------------
📘 Setup FastAPI + MySQL without Docker  
-----------------------------------------------------------------------------------------------

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


