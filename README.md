# StudyFlow

A REST API for an online learning platform built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

StudyFlow allows teachers to create courses and students to enroll in them.

> 🚧 This project is currently under active development.

---

# Features

### Authentication

* User registration
* JWT authentication *(coming soon)*

### User

* View current profile
* Update profile
* Delete account

### Course

* Create course
* Get course information
* Search courses
* Update course
* Delete course

### Enrollment

* Enroll in a course
* Leave a course
* View enrolled courses
* View students in a course

---

# Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy 2.0
* PostgreSQL
* Alembic
* Pydantic v2
* JWT Authentication *(coming soon)*

---

# Project Structure

```text
app/
├── api/
├── core/
├── crud/
├── models/
├── schemas/
├── enums/
├── dependencies.py
└── main.py
```

---

# Database Models

* User
* Course
* Enrollment

Relationships:

* One Teacher → Many Courses
* Many Students ↔ Many Courses (Enrollment)

---

# API

The API design is documented in:

```text
API_PLAN.md
```

---

# Current Progress

* [x] Database models
* [x] Alembic migrations
* [x] Pydantic schemas
* [x] CRUD operations
* [x] Dependencies
* [ ] API routers
* [ ] JWT authentication
* [ ] Role-based authorization
* [ ] Exception handling
* [ ] Testing

---

# Future Improvements

* Pagination
* Course search
* Refresh Tokens
* Docker
* Unit Tests
* CI/CD

---

# Author

**abdurakhman**
