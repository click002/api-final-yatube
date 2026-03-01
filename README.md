# API для Yatube

REST API для социальной сети Yatube. Позволяет создавать посты, комментировать их, подписываться на авторов и многое другое.



## Как установить и запустить

### 1. Клонируйте репозиторий

git clone <ссылка_на_ваш_репозиторий>
cd api_final_yatube
2. Создайте виртуальное окружение и активируйте его
bash
Для Windows
python -m venv venv
venv\Scripts\activate

Для Mac/Linux
python3 -m venv venv
source venv/bin/activate
### 3. Установите зависимости
bash
pip install -r requirements.txt
### 4. Выполните миграции и создайте суперпользователя
bash
python manage.py migrate
python manage.py createsuperuser   # введите имя и пароль
### 5. Запустите сервер
bash
python manage.py runserver
Сервер запустится по адресу: http://127.0.0.1:8000/

# Как пользоваться API (через Postman)
Все запросы отправляются на http://127.0.0.1:8000/api/v1/...

### 1. Получите токен доступа
Запрос:

Метод: POST

URL: http://127.0.0.1:8000/api/v1/jwt/create/

Body: выберите raw и формат JSON

Вставьте:

json
{
    "username": "admin",
    "password": "пароль_который_ввели_при_createsuperuser"
}
Ответ: вы получите два токена - access и refresh. Скопируйте access токен - он понадобится для следующих запросов.

### 2. Создайте новый пост
Запрос:

Метод: POST

URL: http://127.0.0.1:8000/api/v1/posts/

Headers: добавьте строку

text
Authorization: Bearer ваш_access_токен
Body: raw → JSON

json
{
    "text": "Мой первый пост!"
}
Ответ: вы увидите созданный пост с его id, датой публикации и вашим именем автора.

### 3. Посмотрите все посты
Запрос:

Метод: GET

URL: http://127.0.0.1:8000/api/v1/posts/

Токен не нужен - посты может читать кто угодно.

### 4. Измените свой пост
Запрос:

Метод: PATCH

URL: http://127.0.0.1:8000/api/v1/posts/1/ (где 1 - id поста)

Headers: Authorization: Bearer ваш_access_токен

Body:

json
{
    "text": "Обновленный текст поста"
}
### 5. Добавьте комментарий к посту
Запрос:

Метод: POST

URL: http://127.0.0.1:8000/api/v1/posts/1/comments/

Headers: Authorization: Bearer ваш_access_токен

Body:

json
{
    "text": "Отличный пост!"
}
### 6. Подпишитесь на другого пользователя
Сначала создайте еще одного пользователя через админку или командой:

bash
python manage.py shell
from django.contrib.auth.models import User
User.objects.create_user('petr', 'petr@test.com', 'pass123')
Запрос на подписку:

Метод: POST

URL: http://127.0.0.1:8000/api/v1/follow/

Headers: Authorization: Bearer ваш_access_токен

Body:

json
{
    "following": "petr"
}
### 7. Посмотрите на кого вы подписаны
Запрос:

Метод: GET

URL: http://127.0.0.1:8000/api/v1/follow/

Headers: Authorization: Bearer ваш_access_токен

Документация
После запуска сервера полная документация доступна по адресу:
http://127.0.0.1:8000/redoc/

Там описаны все возможные запросы, форматы данных и коды ответов.

Важно!
Access токен живет 24 часа. Когда истечет, получите новый через тот же /jwt/create/

Чужие посты можно читать, но нельзя изменять или удалять

Нельзя подписаться на самого себя

Если что-то не работает - проверьте, что сервер запущен и токен передан правильно
