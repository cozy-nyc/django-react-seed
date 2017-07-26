## Dockerized Django+React starter project

### Requirements
* [Docker Engine](https://docs.docker.com/engine/installation)
* [Docker Compose](https://docs.docker.com/compose/install)

### Stack
* Database: Postgres
* Backend: Django + Django Rest Framework
* Frontend: React
* [Blank] js testing
* Pytest for python testing

### Setup and customize

```
git remote add seed https://github.com/cozy-nyc/django-react-seed.git
git pull seed master
cp server/web/settings/local.py.example server/web/settings/local.py
```

1. Edit the environement variables in `env/dev`
2. Create env/dev with the following values filled

```
DJANGO_SECRET_KEY
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
EMAIL_BACKEND
EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
EMAIL_PORT
EMAIL_USE_TLS
```

Finally, build and start the docker containers:

```
./bin/develop
```

### Run Django commands

```
./bin/django [command]
./bin/django createsuperuser
./bin/django makemigrations [app_name]
```

### Todo
* Dockerized deployment
* Dockerized testing
