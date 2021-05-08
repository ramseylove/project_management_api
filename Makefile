.PHONY: init ci analyze dev_req req build_dev up down rebuild migrate superuser

init:
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
	poetry install
analyze:
	pipenv run flake8 .
	pipenv run isort -v
dev_req:
	pipenv lock -r --dev-only --keep-outdated > requirements-dev.txt
req:
	pipenv lock -r --keep-outdated --requirements > requirements.txt
build_dev:
	pipenv lock -r --dev-only --keep-outdated > requirements-dev.txt
	docker-compose -f docker-compose-dev.yml build
up:
	docker-compose -f docker-compose-dev.yml up
down:
	docker-compose -f docker-compose-dev.yml down
migrate:
	docker-compose -f docker-compose-dev.yml run --rm web python manage.py migrate
superuser:
	docker-compose -f docker-compose-dev.yml run --rm web python manage.py createsuperuser

