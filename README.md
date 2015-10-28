# docker-django
A dockerised generic django instance, with postgres and, eventually, apache.

Initally set up with reference to https://docs.docker.com/compose/django/

This will set up 2 containers - app1-web and app1-db, containing the Django development webserver (NOT TO BE USED IN PRODUCTION) and a postgres server. 

GET DOCKER RUNNING IN OSX:
 - Follow the install procedure at the Docker site
 - Get the docker 'default' machine running. To check this:
    docker-machine ls
 - If it is, import its env variables to your shell:
    eval "$(docker-machine env default)"

TO SET UP DJANGO:
 - Change the postgres settings (User and password) in docker-compose.yml.
 - Change, if you like, the app name from app1
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
 - Start the containers:
    docker-compose up
