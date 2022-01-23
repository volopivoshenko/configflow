======================================
Welcome to configflow's documentation!
======================================

.. image:: _static/assets/logo.png
    :scale: 20 %
    :align: center

.. raw:: html
    <hr>

.. image:: https://img.shields.io/badge/License-MIT-red
.. image:: https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue
.. image:: https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg
.. image:: https://img.shields.io/badge/docstrings-reStructuredText-gree.svg

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
.. image:: https://img.shields.io/badge/%20imports-pycln-%231674b1?style=flat&labelColor=ef8336
.. image:: https://img.shields.io/badge/style-wemake-000000.svg
.. image:: https://img.shields.io/badge/mypy-checked-blue

.. image:: https://github.com/volodymyrPivoshenko/configflow/actions/workflows/integration.yaml/badge.svg
.. image:: https://github.com/volodymyrPivoshenko/configflow/actions/workflows/deployment.yaml/badge.svg
.. image:: https://readthedocs.org/projects/configflow/badge/?version=latest
.. image:: https://badge.fury.io/py/configflow.svg

.. image:: https://codecov.io/gh/volodymyrPivoshenko/configflow/branch/main/graph/badge.svg?token=yyck08xfTN
.. image:: https://img.shields.io/lgtm/alerts/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18
.. image:: https://img.shields.io/lgtm/grade/python/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18

.. image:: https://img.shields.io/github/issues/volodymyrPivoshenko/configflow
.. image:: https://img.shields.io/github/issues-pr/volodymyrPivoshenko/configflow
.. image:: https://img.shields.io/github/contributors/volodymyrPivoshenko/configflow
.. image:: https://img.shields.io/github/last-commit/volodymyrPivoshenko/configflow.svg

.. toctree::
    :maxdepth: 1
    :caption: Table of Contents



=============================
Installation and requirements
=============================

Base requirements
-----------------

.. literalinclude:: ../pyproject.toml
    :language: toml
    :lines: 53-60
    :linenos:

Installation
------------

.. code-block:: bash

    pip install -U configflow --no-cahce-dir
