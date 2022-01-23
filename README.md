<!--suppress HtmlDeprecatedAttribute -->

<div align="center">
    <a><img alt="logo" src="docs/_static/assets/logo.png" height=400></a>
</div>

<p align="center">
    <a><img alt="license" src="https://img.shields.io/badge/License-MIT-red"></a>
    <a><img alt="python" src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue"></a>
    <a><img alt="sphinx" src="https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg"></a>
    <a><img alt="docstrings" src="https://img.shields.io/badge/docstrings-reStructuredText-gree.svg"></a>
</p>

<p align="center">
    <a><img alt="black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
    <a><img alt="isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
    <a><img alt="pycln" src="https://img.shields.io/badge/%20imports-pycln-%231674b1?style=flat&labelColor=ef8336"></a>
    <a><img alt="wemake" src="https://img.shields.io/badge/style-wemake-000000.svg"></a>
    <a><img alt="mypy" src="https://img.shields.io/badge/mypy-checked-blue"></a>
</p>

<p align="center">
    <a><img alt="ci" src=https://github.com/volodymyrPivoshenko/configflow/actions/workflows/integration.yaml/badge.svg?branch=main></a>
    <a><img alt="cd" src=https://github.com/volodymyrPivoshenko/configflow/actions/workflows/deployment.yaml/badge.svg?branch=main></a>
    <a href="https://configflow.readthedocs.io/en/latest/?badge=latest"><img alt="documentation" src="https://readthedocs.org/projects/configflow/badge/?version=latest"/></a>
    <a href="https://badge.fury.io/py/configflow"><img alt="pypi" src="https://badge.fury.io/py/configflow.svg"></a>
</p>

<p align="center">
    <a><img alt="codecov" src="https://codecov.io/gh/volodymyrPivoshenko/configflow/branch/main/graph/badge.svg?token=yyck08xfTN"/></a>
    <a href="https://lgtm.com/projects/g/volodymyrPivoshenko/configflow/alerts/"><img alt="lgtm" src="https://img.shields.io/lgtm/alerts/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18"/></a>
    <a href="https://lgtm.com/projects/g/volodymyrPivoshenko/configflow/context:python"><img alt="language grade" src="https://img.shields.io/lgtm/grade/python/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18"/></a>
</p>

<p align="center">
    <a href="https://github.com/volodymyrPivoshenko/configflow/issues"><img alt="issues" src="https://img.shields.io/github/issues/volodymyrPivoshenko/configflow"></a>
    <a href="https://github.com/volodymyrPivoshenko/configflow/pulls"><img alt="prs" src="https://img.shields.io/github/issues-pr/volodymyrPivoshenko/configflow"></a>
    <a href="https://github.com/volodymyrPivoshenko/configflow/graphs/contributors"><img alt="contributors" src="https://img.shields.io/github/contributors/volodymyrPivoshenko/configflow"></a>
    <a href="https://github.com/volodymyrPivoshenko/configflow/commits/master"><img alt="commit" src="https://img.shields.io/github/last-commit/volodymyrPivoshenko/configflow.svg"></a>
</p>

<hr class="solid">

# Overview

`configflow` – is the configuration management library for Python. It easily allows you to:

- Load your configuration from config files, environment variables, command-line arguments and more
  sources.
- Transform the loaded data into the desired format and validate it.
- Access the results as `Python dataclass-like objects` with full IDE support.
- Make your codebase very flexible by the usage of:

    - Multiple environments.
    - Singletons with lazy loading.
    - Config changes for the unit tests.
    - Custom config sources.

# Installation

Installation is as simple as:

```bash
pip install -U configflow
poetry add configflow
```

`configflow` is also available on conda under the `conda-forge` channel:

```bash
conda install configflow -c conda-forge
```

### Optional dependencies

`configflow` has next optional dependencies:

- If you are using [`Vault by HashiCorp`](https://www.vaultproject.io/) as a config source you can add [`hvac`](https://pypi.org/project/hvac/).

To install these along with `configflow`:

```bash

pip install -U "configflow[hvac]"
poetry add "configflow[hvac]"
```

Of course, you can also install these requirements manually with `pip install ...`.

# See Also

