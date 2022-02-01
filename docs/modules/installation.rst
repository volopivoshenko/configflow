=============================
Installation and requirements
=============================

.. contents::

Base requirements
-----------------

.. literalinclude:: ../pyproject.toml
    :language: toml
    :lines: 53-60
    :linenos:

Installation
------------

Installation is as simple as:

.. code-block:: bash

    pip install -U configflow

    poetry add configflow

Optional dependencies
^^^^^^^^^^^^^^^^^^^^^

``configflow`` has next optional dependencies:

- If you are using `Vault by HashiCorp`_ as a config source you can add `hvac`_.

To install these along with ``configflow``:

.. code-block:: bash

    pip install -U "configflow[hvac]"
    poetry add "configflow[hvac]"

Of course, you can also install these requirements manually with ``pip install ...``.

.. _Vault by HashiCorp: https://www.vaultproject.io/
.. _hvac: https://pypi.org/project/hvac/
