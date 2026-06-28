# StudyFlow

Backend для платформы онлайн-обучения.

## Стек

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT

## Возможности

- Регистрация
- Авторизация
- Создание курсов
- Запись студентов на курс

## Структура проекта

app/
├── models/
├── schemas/
├── crud/
├── api/
└── core/

## Как запустить

1. git clone ...
2. pip install -r requirements.txt
3. alembic upgrade head
4. uvicorn app.main:app --reload