.PHONY: install update demo shadcn-ui tailwind

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

demo : $(VENV)/bin/uv
	$(PYTHON) -m uvicorn demo.app:app --reload

shadcn-ui:
	cd shadcn-ui && npm run dev

tailwind:
	cd shadcn-ui && npm run tailwind
