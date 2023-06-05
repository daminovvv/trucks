FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
COPY django.sh /code/
RUN chmod +x django.sh
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000
