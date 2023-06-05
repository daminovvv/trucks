FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev  # Install gcc compiler and musl-dev

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
COPY django.sh /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000
