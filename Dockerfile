FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apk add --no-cache build-base openldap-dev python2-dev python3-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
