.PHONY: clean
clean: clean-python-cache clean-linters-cache clean-tests-cache clean-docs

.PHONY: lint
lint: lint-flake8 lint-mypy lint-packages

.PHONY: tests
tests: unittests

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

.PHONY: format
format:
	poetry run pycln --config pyproject.toml .
	poetry run isort --settings-path pyproject.toml .
	poetry run black --config pyproject.toml .
	poetry run mdformat README.md CHANGELOG.md CONTRIBUTING.md SECURITY.md

lint-flake8:
	poetry run pflake8

lint-flake8-html:
	- poetry run pflake8 --format=html --htmldir=.flake8
	open .flake8/index.html

lint-mypy:
	poetry run mypy --config-file pyproject.toml

lint-mypy-html:
	- poetry run mypy --config-file pyproject.toml --html-report .mypy
	open .mypy/index.html

lint-packages:
	poetry check
	poetry run pip check
	poetry run safety check --full-report

unittests:
	poetry run pytest
	mkdir -p docs/_static/assets
	poetry run coverage-badge -o docs/_static/assets/tests_coverage.svg -f

unittests-html:
	poetry run pytest --cov-report html
	mkdir -p docs/_static/assets
	poetry run coverage-badge -o docs/_static/assets/tests_coverage.svg -f
	open htmlcov/index.html

doctests:
	poetry run xdoctest -m src/configflow
