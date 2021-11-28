.ONESHELL:
.PHONY: setup

setup:
	python -m venv venv && \
	pip install pip-tools && \
	pip-compile requirements.in && \
	pip install -r requirements.txt && \
	pre-commit install

install:
	source venv/bin/activate && \
	pip-compile requirements.in && \
	pip install -r requirements.txt

update:
	source venv/bin/activate && \
	pip-compile --upgrade requirements.in && \
	pip install -r requirements.txt && \
	pre-commit autoupdate

run-debug:
	source venv/bin/activate && \
	uvicorn app.api:app \
		--reload \
		--reload-dir app
