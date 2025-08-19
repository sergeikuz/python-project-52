build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

# Convert static asset files
collectstatic:
	uv run python3 manage.py collectstatic --no-input

# Apply any outstanding database migrations
migrate:
	uv run python3 manage.py migrate

lint:
	uv run flake8 task_manager

run:
	uv run python3 manage.py runserver

shell:
	uv run python3 manage.py shell_plus --ipython
test:
	uv run python3 manage.py test
