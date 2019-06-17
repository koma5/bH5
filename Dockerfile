FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    unzip wget sudo less curl git gosu build-essential software-properties-common \
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    # postgresql
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
