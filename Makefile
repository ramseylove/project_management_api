.PHONY: analyze remove_vol build up down migrate migrations superuser collectstatic shell

projectName = project_management_api
dockerComposeFile = docker-compose-dev.yml

analyze:
	pipenv run flake8 .
	pipenv run isort -v
remove_vol:
	docker volume rm $(projectName)_postgres_data
build:
	docker-compose -f $(dockerComposeFile) build
up:
	docker-compose -f $(dockerComposeFile) up
down:
	docker-compose -f $(dockerComposeFile) down
migrations:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py makemigrations $(app)
migrate:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py migrate
superuser:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py createsuperuser
collectstatic:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py collectstatic --no-input
shell:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py shell_plus
dump:
	docker-compose -f $(dockerComposeFile) run --rm web python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 2 > scripts/db_seed_data.json