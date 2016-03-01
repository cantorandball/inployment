FROM ubuntu:14.04

ENV PYTHONUNBUFFERED=1 DISPLAY=:99
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update && apt-get install -y libpq-dev python-dev python3-pip xvfb firefox
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements.txt
ADD . /code/

RUN Xvfb :99 -ac &
