# Makefile
format:
	poetry run ruff format .

lint:
	poetry run ruff check .

typecheck:
	poetry run mypy .

check: lint typecheck

test:
	poetry run pytest

pre-commit: format check test
