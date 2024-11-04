FROM python:3.12.6-slim-bullseye
LABEL authors="Mykola"

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

EXPOSE 8080

CMD flask --app src run -h 0.0.0.0 -p $PORT