FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt
ADD . /code/

#RUN Xvfb :99 -screen 0 1024x768x16 &> xvfb.log  &
