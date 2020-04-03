db-up:
	python manage.py makemigrations
	python manage.py migrate

reset-makemigrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

run:
	python manage.py runserver