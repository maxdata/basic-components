.PHONY: install update shadcn-ui tailwind-shadcn-ui

VENV := $(shell pwd)/.venv
PYTHON := $(VENV)/bin/python
UV := $(VENV)/bin/uv
MKDOCS := $(VENV)/bin/mkdocs

$(VENV)/bin/uv:
	python -m venv $(VENV)
	$(PYTHON) -m pip install uv

install: $(VENV)/bin/uv
	$(UV) sync

docs-backend-dev: $(VENV)/bin/uv
	$(PYTHON) -m muvicorn documentation.backend.app:app --reload --port 10000

docs-frontend-dev: $(MKDOCS)
	cd documentation && $(MKDOCS) serve

shadcn-ui:
	cd shadcn-ui && npm run dev

shadcn-ui-tailwind:
	cd shadcn-ui && npm run tailwind

docs-tailwind:
	cd documentation && npm install && ./node_modules/.bin/tailwindcss -i ./input.css -o ./docs/dist/output.css

docs-backend-prod:
	$(UV) run fastapi run documentation/backend/app.py  --port 10000
