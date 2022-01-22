.PHONY: clean
clean: clean-python-cache clean-linters-cache clean-tests-cache clean-docs

.PHONY: lint
lint: lint-flake8 lint-mypy

.PHONY: tests
tests: unittests doctests

clean-python-cache:
	find . -type f -name *.py[co] -path .tox -prune -delete
	find . -type d -name __pycache__ -path .tox -prune -exec rm -rf {} +

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

.PHONY: format
format:
	pycln --config pyproject.toml .
	isort --settings-path pyproject.toml .
	black --config pyproject.toml .

lint-flake8:
	pflake8

lint-flake8-html:
	- pflake8 --format=html --htmldir=.flake8
	open .flake8/index.html

lint-mypy:
	mypy --config-file pyproject.toml

lint-mypy-html:
	- mypy --config-file pyproject.toml --html-report .mypy
	open .mypy/index.html

tests-coverage-badge:
	mkdir -p docs/_static/assets
	coverage-badge -o docs/_static/assets/tests_coverage.svg

unittests:
	pytest --cov=src -vv
	tests-coverage-badge

unittests-html:
	pytest --cov=src --cov-report html -vv
	tests-coverage-badge
	open htmlcov/index.html

doctests:
	xdoctest -m src/configflow
