FROM python:3.8

MAINTAINER Chris Josh "christopherjoshua25@hotmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /zeno_task/backend

COPY requirements.txt /zeno_task/backend

RUN pip install -r requirements.txt

COPY . /zeno_task/backend

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

