FROM ubuntu:14.04

#RUN apt-get update && apt-get upgrade
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update && apt-get install -y libpq-dev python-dev python3-pip xvfb
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements.txt
ADD . /code/

#RUN Xvfb :99 -screen 0 1024x768x16 &> xvfb.log  &
