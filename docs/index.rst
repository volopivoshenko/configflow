======================================
Welcome to configflow's documentation!
======================================

.. image:: _static/assets/logo.png
    :alt: logo
    :scale: 20 %
    :align: center

|

.. image:: https://img.shields.io/badge/License-MIT-red
    :alt: license
.. image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue
    :alt: python
.. image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
    :alt: sphinx
.. image:: https://img.shields.io/badge/docstrings-reStructuredText-gree.svg
    :alt: docstrings
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: black
.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :alt: isort
.. image:: https://img.shields.io/badge/%20imports-pycln-%231674b1?style=flat&labelColor=ef8336
    :alt: pycln
.. image:: https://img.shields.io/badge/style-wemake-000000.svg
    :alt: wemake
.. image:: https://img.shields.io/badge/mypy-checked-blue
    :alt: mypy
.. image:: https://github.com/volodymyrPivoshenko/configflow/actions/workflows/integration.yaml/badge.svg
    :alt: ci
.. image:: https://github.com/volodymyrPivoshenko/configflow/actions/workflows/deployment.yaml/badge.svg
    :alt: cd
.. image:: https://readthedocs.org/projects/configflow/badge/?version=latest
    :alt: docs
.. image:: https://badge.fury.io/py/configflow.svg
    :alt: pypi
.. image:: https://codecov.io/gh/volodymyrPivoshenko/configflow/branch/main/graph/badge.svg?token=yyck08xfTN
    :alt: coverage
.. image:: https://img.shields.io/lgtm/alerts/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18
    :alt: alerts
.. image:: https://img.shields.io/lgtm/grade/python/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18
    :alt: lgtm
.. image:: https://img.shields.io/github/issues/volodymyrPivoshenko/configflow
    :alt: issues
.. image:: https://img.shields.io/github/issues-pr/volodymyrPivoshenko/configflow
    :alt: pr
.. image:: https://img.shields.io/github/contributors/volodymyrPivoshenko/configflow
    :alt: contributors
.. image:: https://img.shields.io/github/last-commit/volodymyrPivoshenko/configflow.svg
    :alt: commits

Overview
========

``configflow`` – is the configuration management library for Python. It easily allows you to:

- Load your configuration from config files, environment variables, command-line arguments and more sources.
- Transform the loaded data into the desired format and validate it.
- Access the results as ``Python dataclass-like objects`` with full IDE support.
- Make your codebase very flexible by the usage of:

  - Multiple environments.
  - Singletons with lazy loading.
  - Config changes for the unit tests.
  - Custom config sources.

Examples
========

.. TODO add examples

See Also
========

.. TODO add references

.. toctree::
    :maxdepth: 1
    :caption: Table of Contents

    modules/installation.rst
    api/misc.string.rst
