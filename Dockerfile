FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/
COPY django.sh /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN chmod +x django.sh
CMD ["./django.sh"]

EXPOSE 8000
