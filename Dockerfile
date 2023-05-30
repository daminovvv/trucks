FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN python manage.py migrate

RUN python manage.py shell -c  \
    "from trucksapp.services import load_csv, create_cars; load_csv(); create_cars()"

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]