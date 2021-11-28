.ONESHELL:
.PHONY: setup

setup:
	python -m venv venv && \
	pip install pip-tools && \
	pip-compile requirements.in && \
	pip install -r requirements.txt && \
	pre-commit install

install:
	pip-compile requirements.in && \
	pip install -r requirements.txt && \
	pre-commit autoupdate
