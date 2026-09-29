# Yatube API

**REST API для социальной сети блогов Yatube**

Yatube API предоставляет разработчикам возможность интегрироваться с платформой Yatube, автоматизировать задачи и создавать собственные клиенты.

---

## Основные функции

- **Управление постами**: создание, чтение, обновление и удаление публикаций.
- **Комментирование**: возможность оставлять комментарии к постам и управлять ими.
- **Сообщества (группы)**: просмотр списка сообществ и информации о них.
- **Подписки (follow)**: подписка на других авторов, просмотр своих подписок и поиск по ним.
- **Аутентификация**: безопасный доступ к API с помощью JWT-токенов.

---

## Технологический стек

- Python 3.9+
- Django 3.2
- Django REST Framework
- Djoser & Simple JWT
- SQLite

---

## Установка и запуск

1. **Клонируйте репозиторий** (или скопируйте файлы проекта).

2. **Создайте и активируйте виртуальное окружение**:

   ```bash
   python -m venv venv
   source venv/bin/activate      # для Linux/Mac
   venv\Scripts\activate          # для Windows
   ```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Выполните миграции**:

   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя** (для доступа в админку и тестирования):

   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер**:

   ```bash
   python manage.py runserver
   ```

Сервер запустится по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Примеры использования API

**Базовый URL:** `http://127.0.0.1:8000/api/v1/`

### Получение токена

**Запрос:**  
`POST /jwt/create/`

```json
{
    "username": "admin",
    "password": "ваш_пароль"
}
```

**Ответ:**

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Создание поста

**Запрос:**  
`POST /posts/`  
**Headers:**  
`Authorization: Bearer <ваш_access_токен>`

```json
{
    "text": "Мой первый пост!"
}
```

**Ответ:**

```json
{
    "id": 1,
    "author": "admin",
    "text": "Мой первый пост!",
    "pub_date": "2024-03-01T12:00:00Z",
    "image": null,
    "group": null
}
```

### Получение списка постов

**Запрос:**  
`GET /posts/?limit=2&offset=0`

**Ответ:**

```json
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "admin",
            "text": "Мой первый пост!",
            "pub_date": "2024-03-01T12:00:00Z",
            "image": null,
            "group": null
        }
    ]
}
```

### Добавление комментария

**Запрос:**  
`POST /posts/1/comments/`  
**Headers:**  
`Authorization: Bearer <ваш_access_токен>`

```json
{
    "text": "Отличный пост!"
}
```

**Ответ:**

```json
{
    "id": 1,
    "author": "admin",
    "text": "Отличный пост!",
    "created": "2024-03-01T12:05:00Z",
    "post": 1
}
```

### Подписка на пользователя

**Запрос:**  
`POST /follow/`  
**Headers:**  
`Authorization: Bearer <ваш_access_токен>`

```json
{
    "following": "parker"
}
```

**Ответ:**

```json
{
    "user": "admin",
    "following": "parker"
}
```

### Просмотр подписок

**Запрос:**  
`GET /follow/`  
**Headers:**  
`Authorization: Bearer <ваш_access_токен>`

**Ответ:**

```json
[
    {
        "user": "admin",
        "following": "parker"
    }
]
```

---

## Документация

Подробная документация (ReDoc) доступна по адресу:  
[http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## Важно

- **Access токен** живёт **24 часа**.
- **Чужие посты** можно только читать (редактирование/удаление недоступно).
- Нельзя подписаться **на самого себя**.

---

## Автор

**Nikita Filin**  
GitHub: [@click002](https://github.com/click002)
