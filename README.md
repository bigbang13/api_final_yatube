# api_final

### REST API YATUBE
Позволяет аутентифицированным пользователям изменять и удалять свой контент. Осуществляет получение информации о группах, пользователях, их постах и комментариям к ним.

## Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/bigbang13/api_final_yatube.git
cd api_final_yatube
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate
```
3. Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Выполнить миграции:
```
python manage.py migrate
```
5. Запустить проект:
```
python manage.py runserver
```
Документация после запуска доступна по адресу ```http://127.0.0.1:8000/redoc/```.

## Технологии
- Python 3.7
- Django 2.2.16
- Django REST Framework 3.12.4

### Автор

_Рябов В.С._
_email: ryabov.v.s@yandex.ru_
_github: https://github.com/bigbang13_
