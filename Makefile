.PHONY: init ci analyze build rebuild migrate lang-make lang-compile

init:
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	poetry install
analyze:
	pipenv run flake8 .
	pipenv run isort -v
build:
	docker-compose -f docker-compose-withdb.yml build
up:
	docker-compose -f local.yml up
migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate
superuser:
	docker-compose -f docker-compose-prod.yml run --rm web python manage.py createsuperuser

