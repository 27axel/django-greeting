# Django Greeting App

Простое веб-приложение на Django, которое приветствует пользователей по имени.

## Возможности

- Форма ввода имени с валидацией
- Сохранение имён в базу данных SQLite
- Персонализированное приветствие
- Отображение последнего вошедшего пользователя
- CSRF-защита
- Современный адаптивный дизайн

## Требования

- Python 3.8+
- Django 4.2+

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone git@github.com:27axel/django-greeting.git
cd DjangoProject
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# или
.venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install django
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

6. Откройте браузер и перейдите по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта

```
├── config/          # Конфигурация проекта (settings, urls, wsgi, asgi)
├── greeting/        # Приложение: модели, представления, формы
├── templates/       # HTML-шаблоны
├── manage.py        # Утилита управления Django
└── db.sqlite3       # База данных SQLite
```

## Админ-панель

Для доступа к админ-панели создайте суперпользователя:
```bash
python manage.py createsuperuser
```
Затем перейдите на [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
