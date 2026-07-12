# StudyFlow

StudyFlow is a backend application for an online learning platform built with **FastAPI**.

The platform supports two roles:

- 👨‍🏫 Teacher — creates and manages courses.
- 👨‍🎓 Student — enrolls in courses and views enrolled courses.

This project was created as a portfolio project to demonstrate backend development skills using modern Python technologies.

---

# Features

## Authentication

- JWT Authentication
- OAuth2 Password Flow
- Password hashing
- Protected endpoints
- Current user endpoint (`/me`)

## User

- Register
- Login
- View profile
- Update profile
- Delete account

## Courses

Teacher can:

- Create course
- Update own course
- Delete own course

Everyone can:

- View all courses
- Search courses by title
- View course details

## Enrollment

Student can:

- Enroll in a course
- Leave a course
- View enrolled courses

Everyone can:

- View students enrolled in a course

---

# Tech Stack

Backend

- Python 3.13
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Alembic
- Pydantic v2

Authentication

- JWT
- OAuth2
- pwdlib

Development

- Uvicorn
- Swagger UI

---

# Project Structure

```
app/
│
├── api/
├── crud/
├── core/
├── models/
├── schemas/
├── enums/
├── dependencies.py
└── main.py

alembic/

requirements.txt
README.md
```

---

# Database

Main entities:

- User
- Course
- Enrollment

Relationships

```text
Teacher (User)
      1
      │
      │ creates
      │
      *
    Course
      1
      │
      │ has
      │
      *
 Enrollment
      *
      │
      │ belongs to
      │
      1
Student (User)
```

---

# API Endpoints

## Authentication

| Method | Endpoint |
|---------|-----------|
| POST | `/auth/register` |
| POST | `/auth/login` |

---

## User

| Method | Endpoint |
|---------|-----------|
| GET | `/me` |
| PATCH | `/me` |
| DELETE | `/me` |

---

## Courses

| Method | Endpoint |
|---------|-----------|
| POST | `/courses` |
| GET | `/courses` |
| GET | `/courses/{id}` |
| GET | `/courses/title` |
| PATCH | `/courses/{id}` |
| DELETE | `/courses/{id}` |

---

## Enrollment

| Method | Endpoint |
|---------|-----------|
| POST | `/me/courses` |
| GET | `/me/courses` |
| DELETE | `/me/courses/{course_id}` |
| GET | `/courses/{course_id}/students` |

---

# Authentication

All protected endpoints require a JWT access token.

```
Authorization: Bearer <access_token>
```

---

# Getting Started

Clone the repository

```bash
git clone https://github.com/your_username/StudyFlow.git
cd StudyFlow
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Run

```bash
uvicorn app.main:app --reload
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

---

# Current Status

✅ Backend completed

- Authentication
- Authorization
- CRUD operations
- Role permissions
- Course enrollment
- PostgreSQL integration
- Swagger documentation

🚧 Frontend is currently under development.

---

# Future Improvements

- React + TypeScript frontend
- Responsive UI
- Docker
- Unit tests
- CI/CD
- File upload
- Course thumbnails

---

