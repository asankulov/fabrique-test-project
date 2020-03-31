FROM python:3.8-buster

WORKDIR /usr/src/app
COPY Pipfile .
COPY Pipfile.lock .

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install build-essential gcc python-dev -y

RUN pip install uwsgi
RUN pip install pipenv
RUN pipenv install

COPY . .
RUN chmod +x runserver.sh

CMD ./runserver.sh
