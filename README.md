# docker-django
A dockerised generic django instance, with mysql and apache.

Initally set up with reference to https://docs.docker.com/compose/django/

This will set up 2 containers - app1-web and app1-db, containing the Django development webserver (NOT TO BE USED IN PRODUCTION) and a postgres server. 

TO SET UP DJANGO:
 - Create the django project:
    docker-compose run app1-web django-admin.py startproject yourprojectname .
 - Start the containers:
    docker-compose up
