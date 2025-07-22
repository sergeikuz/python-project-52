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

run:
	uv run python3 manage.py runserver
