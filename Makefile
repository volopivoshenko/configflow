.PHONY: clean
clean: clean-python-cache clean-linters-cache clean-tests-cache clean-docs

.PHONY: lint
lint: lint-flake8 lint-mypy

.PHONY: tests

.PHONY: format

clean-python-cache:
	find . -type f -name *.py[co] -delete
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf dist

clean-tests-cache:
	rm -rf .pytest
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

clean-linters-cache:
	rm -rf .flake8
	rm -rf .mypy
	rm -rf .mypy_cache

clean-docs:
	rm -rf docs/_build
	rm -rf docs/_sources

format:
	poetry run isort --settings-path pyproject.toml .
	poetry run black --config pyproject.toml .

lint-flake8:
	poetry run pflake8 --config pyproject.toml

lint-mypy:
	poetry run mypy --config-file pyproject.toml

lint-packages:
	poetry check
	poetry run safety check --full-report

tests:
	poetry run pytest
