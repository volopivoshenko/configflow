.PHONY: clean
clean: clean-python-cache clean-linters-cache clean-tests-cache clean-distributions clean-docs

.PHONY: lint
lint: lint-flake8 lint-mypy

.PHONY: tests
tests: unittests doctests

clean-python-cache:
	find . -type f -name *.py[co] -delete
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +

clean-tests-cache:
	find . -type d -name .pytest -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name htmlcov -exec rm -rf {} +
	find . -type f -name .coverage -exec rm -rf {} +

clean-linters-cache:
	find . -type d -name .flake8 -exec rm -rf {} +
	find . -type d -name .mypy -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +

clean-distributions:
	find . -type d -name build -exec rm -rf {} +
	find . -type d -name dist -exec rm -rf {} +

clean-docs:
	find . -type d -name _build -exec rm -rf {} +

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

unittests:
	pytest --cov=src -vv
	find . -type f -name tests_coverage.svg -exec rm -rf {} +
	mkdir -p _docs/_static/assets
	coverage-badge -o _docs/_static/assets/tests_coverage.svg

unittests-html:
	pytest --cov=src --cov-report html -vv
	open htmlcov/index.html
	find . -type f -name tests_coverage.svg -exec rm -rf {} +
	mkdir -p _docs/_static/assets
	coverage-badge -o _docs/_static/assets/tests_coverage.svg

doctests:
	xdoctest -m src/configflow
