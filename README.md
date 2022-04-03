<!--suppress HtmlDeprecatedAttribute -->
<div align="center">
  <a href="https://pypi.org/project/configflow">
    <img alt="logo" src="https://github.com/volodymyrPivoshenko/configflow/blob/main/docs/_static/assets/logo.svg?raw=True" height=200>
  </a>
</div>

<p align="center">
  <a href="https://choosealicense.com/licenses/mit">
    <img alt="license" src="https://img.shields.io/badge/License-MIT-red">
  </a>
  <a href="https://pypi.org/project/configflow">
    <img alt="python" src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue">
  </a>
  <a href="https://www.sphinx-doc.org/en/master">
    <img alt="sphinx" src="https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg">
  </a>
  <a href="https://numpydoc.readthedocs.io/en/latest/format.html">
    <img alt="docstrings" src="https://img.shields.io/badge/docstrings-numpy-gree.svg">
  </a>
</p>

<p align="center">
  <a href="https://github.com/psf/black">
    <img alt="black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://pycqa.github.io/isort/index.html">
    <img alt="isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336">
  </a>
  <a href="https://hadialqattan.github.io/pycln">
    <img alt="pycln" src="https://img.shields.io/badge/%20imports-pycln-%231674b1?style=flat&labelColor=ef8336">
  </a>
  <a href="https://wemake-python-stylegui.de/en/latest/index.html">
    <img alt="wemake" src="https://img.shields.io/badge/style-wemake-000000.svg">
  </a>
  <a href="https://mypy.readthedocs.io/en/stable/index.html">
    <img alt="mypy" src="https://img.shields.io/badge/mypy-checked-blue">
  </a>
  <a href="https://github.com/pyupio/safety">
    <img alt="safety" src="https://img.shields.io/badge/safety-checked-blue">
  </a>
  <a href="https://github.com/semantic-release/semantic-release">
    <img alt="semantic_release" src="https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release">
  </a>
</p>

<p align="center">
  <a href="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/integration.yaml">
    <img alt="integration" src="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/integration.yaml/badge.svg">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/deployment.yaml">
    <img alt="deployment" src="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/deployment.yaml/badge.svg">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/codeql.yaml">
    <img alt="codeql" src="https://github.com/volodymyrPivoshenko/configflow/actions/workflows/codeql.yaml/badge.svg">
  </a>
  <a href="https://configflow.readthedocs.io/en/latest">
    <img alt="docs" src="https://readthedocs.org/projects/configflow/badge/?version=latest">
  </a>
  <a href="https://pypi.org/project/configflow">
    <img alt="pypi" src="https://badge.fury.io/py/configflow.svg">
  </a>
</p>

<p align="center">
  <a href="https://codecov.io/gh/volodymyrPivoshenko/configflow">
    <img alt="coverage" src="https://codecov.io/gh/volodymyrPivoshenko/configflow/branch/main/graph/badge.svg?token=yyck08xfTN"/>
  </a>
  <a href="https://lgtm.com/projects/g/volodymyrPivoshenko/configflow/alerts/">
    <img alt="lgtm" src="https://img.shields.io/lgtm/alerts/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18"/>
  </a>
  <a href="https://lgtm.com/projects/g/volodymyrPivoshenko/configflow/context:python">
    <img alt="lgtm" src="https://img.shields.io/lgtm/grade/python/g/volodymyrPivoshenko/configflow.svg?logo=lgtm&logoWidth=18"/>
  </a>
  <a href="https://codeclimate.com/github/volodymyrPivoshenko/configflow/maintainability">
    <img alt="codeclimate" src="https://api.codeclimate.com/v1/badges/c51574700d1cef487866/maintainability">
  </a>
</p>

<p align="center">
  <a href="https://github.com/volodymyrPivoshenko/configflow/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/volodymyrPivoshenko/configflow">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/issues">
    <img alt="issues" src="https://img.shields.io/github/issues-closed/volodymyrPivoshenko/configflow.svg">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/pulls">
    <img alt="pr" src="https://img.shields.io/github/issues-pr/volodymyrPivoshenko/configflow">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/graphs/contributors">
    <img alt="contributors" src="https://img.shields.io/github/contributors/volodymyrPivoshenko/configflow">
  </a>
  <a href="https://github.com/volodymyrPivoshenko/configflow/commits/main">
    <img alt="commit" src="https://img.shields.io/github/last-commit/volodymyrPivoshenko/configflow.svg">
  </a>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/volo.pivoshenko" target="_blank">
    <img alt="buymeacoffee" src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" height="25" width="100">
  </a>
</p>

# Overview

`configflow` – is the configuration management package. It easily allows you to:

- Load your configuration from files, environment variables, command-line arguments and more
  sources.
- Transform the loaded data into the desired format and validate it
  via [`pydantic`](https://github.com/samuelcolvin/pydantic).
- Access the results
  as [`Python dataclass-like objects`](https://docs.python.org/3/library/dataclasses.html).
- Make your codebase very flexible.

# Installation

Installation is as simple as:

```shell
pip install -U configflow

poetry add configflow
```

### Optional dependencies

`configflow` has next optional dependencies:

- If you are using [`Vault by HashiCorp`](https://www.vaultproject.io/) as a config source you can
  add [`hvac`](https://pypi.org/project/hvac).

To install these along with `configflow`:

```bash

pip install -U "configflow[hvac]"

poetry add "configflow[hvac]"
```

Of course, you can also install these requirements manually with `pip install ... | poetry add ...`.

# Examples

# See Also
