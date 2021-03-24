# DRF_template <!-- omit in toc -->

- [First need to define a $SECRET variable in either a .env file or shell environment.](#first-need-to-define-a-secret-variable-in-either-a-env-file-or-shell-environment)
  - [Create a new secret key in a running django envrionment](#create-a-new-secret-key-in-a-running-django-envrionment)
  - [Create a secret with online tool](#create-a-secret-with-online-tool)
- [Build with docker-compose](#build-with-docker-compose)
  - [Create and Run migrations](#create-and-run-migrations)
  - [create super user](#create-super-user)
- [Dependency Versions](#dependency-versions)

## First need to define a $SECRET variable in either a .env file or shell environment.

### Create a new secret key in a running django envrionment
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Create a secret with online tool
https://djecrety.ir

## Build with docker-compose
```
docker-compose up --build
```

### Create and Run migrations
```
docker-compose exec web python manage.py makemigrations accounts
docker-compose exec web python manage.py migrate
```

### create super user
```
docker-compose exec web python manage.py createsuperuser
```

## Dependency Versions
python = "3.9"
django = "==3.1.7"
psycopg2-binary = "==2.8.6"
djangorestframework = "==3.12.2"