# TO-DO Application (FastAPI + Bootstrap)

Простое TO-DO приложение с REST API и веб-интерфейсом, реализованное на Python с использованием FastAPI.
Позволяет создавать пользователей, проекты, задачи, отмечать задачи выполненными и удалять их.

## Основные возможности

- Создание пользователей

- Создание проектов, привязанных к пользователям

- Добавление задач к проектам

- Отметка задач как выполненных

- Удаление задач

## Технологии

- Python 3.9+

- FastAPI — быстрый фреймворк для API

- Uvicorn — ASGI сервер

- Jinja2 — шаблонизатор

- Bootstrap 5 — фронтенд дизайн

- Pydantic — валидация данных

## Запуск проекта

1. Установите зависимости:

```
pip install fastapi uvicorn jinja2
```

2. Запуск:

```
uvicorn main:app --reload
```

3. Откройте в браузере:

```
http://127.0.0.1:8000/
```
