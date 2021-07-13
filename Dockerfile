FROM python:3

WORKDIR /app
COPY servicedockerized servicedockerized
COPY manage.py manage.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

