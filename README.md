# docker-django
A dockerised generic django instance, with postgres and, eventually, apache.

Initally set up with reference to https://docs.docker.com/compose/django/

This will set up 2 containers - app1-web and app1-db, containing the Django development webserver (NOT TO BE USED IN PRODUCTION) and a postgres server. 

GET DOCKER RUNNING IN OSX:
 - Follow the install procedure at the Docker site. 
 - Start the default machine running using the 'Docker quickstart terminal' app
 - Get the docker 'default' machine running. To check this:
    docker-machine ls
   and look for a macine called 'default' in state 'Running'
 - If it is, import its env variables to your shell:
    eval "$(docker-machine env default)"

START DOCKER CONTAINERS:
 - Start the containers:
    docker-compose up
 - Check they're running: 
    docker ps
   or, to list non-running containers too:
    docker ps -a
   For this project, you're looking for containers called appname-web_1 and appname-db1

CONNECT TO THE DJANGO SITE:
 - Get the ip for your Docker container:
    docker-machine ip default 
 - You can then connect to the Django site on dockermachineip:8000

TO SET UP DJANGO: (You don't need to do this if there's already an 'Inplyoment project in this folder - primarily here for future reference)
 - Change the postgres settings (User and password) in docker-compose.yml.
 - In the same file, if you like, you can also change the app name from app1
 - Create the django project:
    docker-compose run app1-web django-admin.py startproject yourprojectname .
 - Configure yourprojectname/settings.py to point to our db server:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    	'NAME': 'whateveryourpostgresusernamewas',
		'USER': 'whateveryourpostgresusernamewas',
        'PASSWORD': 'whateveryourpostgrespasswordis',
		'HOST': 'app1-db',
		'PORT': 5432,
	}
}
```
