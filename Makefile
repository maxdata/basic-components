
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

lint:
	poetry run ruff check .

lint-fix:
	poetry run ruff check --fix --unsafe-fixes .

format-python:
	poetry run ruff format .

format-prettier:
	npx prettier components --write

format: format-python format-prettier

type-check:
	poetry run pyright

run:
	poetry run fastapi run app.py  --port 10000

dev:
	poetry run fastapi dev app.py  --port 10000
