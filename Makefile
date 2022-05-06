syncdb:  ## apply all migrations and load fixtures
	python manage.py migrate
	python manage.py migrate --run-syncdb
	python manage.py loaddata one_to_one many_to_one many_to_many
