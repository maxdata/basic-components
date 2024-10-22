.PHONY: install update shadcn-ui tailwind-shadcn-ui

VENV := $(shell pwd)/.venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv
MKDOCS := $(VENV)/bin/mkdocs

$(VENV)/bin/uv:
	python -m venv $(VENV)
	$(PYTHON) -m pip install uv

install: $(VENV)/bin/uv
	$(UV) pip install -r requirements.txt

update: $(VENV)/bin/uv
	$(UV) pip compile requirements.txt -o requirements.lock
	$(UV) pip sync requirements.lock

docs-backend: $(VENV)/bin/uv
	$(PYTHON) -m uvicorn documentation.backend.app:app --reload --port 10000

docs-frontend: $(MKDOCS)
	cd documentation && $(MKDOCS) serve

shadcn-ui:
	cd shadcn-ui && npm run dev

tailwind-shadcn-ui:
	cd shadcn-ui && npm run tailwind

setup-tailwind:
	cd documentation && npm install && npx tailwindcss init

build-css:
	cd documentation && npx run build
