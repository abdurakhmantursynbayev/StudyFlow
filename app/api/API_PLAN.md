# StudyFlow API Plan

## Overview

REST API for the StudyFlow backend.

---

## Authentication

|  Method  | Endpoint         | Description                            | Access |
| :------: | ---------------- | -------------------------------------- | ------ |
| **POST** | `/auth/register` | Register a new user                    | Public |
| **POST** | `/auth/login`    | Authenticate user and return JWT token | Public |

---

## User

|   Method   | Endpoint | Description                    | Access        |
| :--------: | -------- | ------------------------------ | ------------- |
|   **GET**  | `/me`    | Get current authenticated user | Authenticated |
|  **PATCH** | `/me`    | Update current user profile    | Authenticated |
| **DELETE** | `/me`    | Delete current user account    | Authenticated |

---

## Course

|   Method   | Endpoint                 | Description             | Access       |
| :--------: | ------------------------ | ----------------------- | ------------ |
|  **POST**  | `/courses`               | Create a new course     | Teacher      |
|   **GET**  | `/courses`               | Get all courses         | Public       |
|   **GET**  | `/courses?title={title}` | Search courses by title | Public       |
|   **GET**  | `/courses/{course_id}`   | Get course details      | Public       |
|  **PATCH** | `/courses/{course_id}`   | Update course           | Course Owner |
| **DELETE** | `/courses/{course_id}`   | Delete course           | Course Owner |

---

## Enrollment

|   Method   | Endpoint                        | Description                           | Access  |
| :--------: | ------------------------------- | ------------------------------------- | ------- |
|  **POST**  | `/me/courses`                   | Enroll in a course                    | Student |
|   **GET**  | `/me/courses`                   | Get all enrolled courses              | Student |
| **DELETE** | `/me/courses/{course_id}`       | Leave a course                        | Student |
|   **GET**  | `/courses/{course_id}/students` | Get all students enrolled in a course | Teacher |

---

## Future Endpoints

These endpoints may be implemented in future versions.

|  Method  | Endpoint                         | Description                              |
| :------: | -------------------------------- | ---------------------------------------- |
|  **GET** | `/teachers/{teacher_id}/courses` | Get all courses created by a teacher     |
|  **GET** | `/users/{user_id}`               | Get public user information (Admin only) |
| **POST** | `/auth/refresh`                  | Refresh JWT access token                 |
| **POST** | `/auth/logout`                   | Logout user                              |

---

## Authorization

### Public

* No authentication required.

### Authenticated

* Any logged-in user.

### Student

* Logged-in user with `student` role.

### Teacher

* Logged-in user with `teacher` role.

### Course Owner

* Teacher who created the course.
