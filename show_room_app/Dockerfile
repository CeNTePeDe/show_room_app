FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/show_room_app

COPY Pipfile Pipfile.lock /usr/src/show_room_app/
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

COPY . .



