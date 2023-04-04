FROM python:3.10-slim

RUN apt-get update && apt-get -y install libpq-dev gcc

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 core.wsgi:application
