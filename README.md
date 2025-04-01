python -m venv venv

.\venv\scripts\activate

pip install django

django-admin startproject core .

python manage.py startapp filmes

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
    - username: sql
    - email: lucaslinyker@outlook.com
    - passowrd: nikond800

