.PHONY: clean lint lint-fix format-python format-prettier format type-check dev install update

VENV := .venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv

$(VENV)/bin/uv:
	python -m venv $(VENV)
	$(PYTHON) -m pip install uv

install: $(VENV)/bin/uv
	$(UV) pip install -r requirements.txt

update: $(VENV)/bin/uv
	$(UV) pip compile requirements.txt -o requirements.lock
	$(UV) pip sync requirements.lock

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

lint: $(VENV)/bin/uv
	$(PYTHON) -m ruff check .

lint-fix: $(VENV)/bin/uv
	$(PYTHON) -m ruff check --fix --unsafe-fixes .

format-python: $(VENV)/bin/uv
	$(PYTHON) -m ruff format .

format-prettier:
	npx prettier components --write

format: format-python format-prettier

type-check: $(VENV)/bin/uv
	$(PYTHON) -m pyright

dev: $(VENV)/bin/uv
	$(PYTHON) -m uvicorn app:app --reload
