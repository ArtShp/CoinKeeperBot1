FROM python:3.8

WORKDIR /home

ENV TELEGRAM_API_TOKEN='1332389210:AAE0Lie1rnaR12W69Fzp7LoPIL08ejpz_Ac'
ENV TELEGRAM_ACCESS_ID='115943804'

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3
COPY *.py ./
COPY createdb.sql ./

ENTRYPOINT ["python", "server.py"]

