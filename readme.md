Описание:
Веб-приложение с API интерфейсом и админ-панелью представляет собой разработку 
онлайн платформы торговой сети электроники.

Сеть представляет собой иерархическую структуру из 3 уровней:

Завод;
Розничная сеть;
Индивидуальный предприниматель.

Стек проекта:

Python
Poetry
Django
DRF
PostgreSQL
Docker
Docker Compose

Документация:

Документация находится по ссылкам:

http://127.0.0.1:8000/api/redoc/ 
http://127.0.0.1:8000/api/swagger/ 

ЗАПУСК ПРОЕКТА ЛОКАЛЬНО.

Клонируйте проект командой:
git clone git@github.com:kanlar75/attestation.git
Активируйте виртуальное окружение командой:
poetry shell
Установите зависимости командой:
poetry install

Создайте Базу данных PostgreSQL командами:

1. psql -U <имя пользователя>
2. CREATE DATABASE <имя базы данных>;
3. \q

Пропишите переменные окружения в файл .env, используйте образец из .env.example
Для локального запуска установите ENV_TYPE='local'

Для миграции в базу данных используйте команду:
python manage.py migrate

Для создания суперпользователя и пользователей используйте команду:
python manage.py create_users
Для создания только суперпользователя используйте команду:
python manage.py createsuperuser

Выполните команду: python manage.py runserver

В адресной стоке браузера введите адрес http://127.0.0.1:8000/api/admin
Пароль и логин для суперпользователя:
login: admin@test.com password: 111

Для всех пользователей (user1@test.com, user2@test.com) password: 111.

ЗАПУСК ПРОЕКТА В DOCKER.

Клонируйте проект командой:
git clone git@github.com:kanlar75/attestation.git

Установите docker и при необходимости docker-compose.
Пропишите переменные окружения в файл .env, используйте образец из .env.example

Создайте образ командой:
docker-compose build

Для запуска в docker установите ENV_TYPE='docker'.

Запустите контейнеры командой:
docker-compose up

В адресной стоке браузера введите адрес http://127.0.0.1:8000/api/admin
Пароль и логин для суперпользователя:
login: admin@test.com password: 111

Для всех пользователей (user1@test.com, user2@test.com) password: 111.

Тестирование выполнялось в Unitest. Покрытие тестами 90%.
Для запуска тестов с расчетом покрытия выполните команды:
coverage run manage.py test
coverage report
