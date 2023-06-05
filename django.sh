#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py shell -c  \
    "from trucksapp.services import load_csv, create_cars; load_csv(); create_cars()"
python manage.py runserver 0.0.0.0:8000
