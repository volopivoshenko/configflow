"""Implementation of the DOTENV IO functions.

This module is a decorator of the ``python-dotenv`` package, because it
doesn't provide common Python IO interface: ``load | loads`` and doesn't
convert data types.
"""

from __future__ import annotations

from io import StringIO
from typing import Any
from typing import Dict
from typing import TextIO

from dotenv import dotenv_values

from configflow import types


def loads(stream: str) -> Dict[Any, Any]:
    r"""Parse the DOTENV stream and produce the corresponding Python object.

    Examples
    --------
    >>> dotenv_stream = "DB_HOST=localhost\nDB_PORT=8080"
    >>> loads(dotenv_stream)
    {'DB_HOST': 'localhost', 'DB_PORT': 8080}
    """

    parsed_values = dict(dotenv_values(stream=StringIO(stream)))
    return types.dictionary.deep_map(parsed_values, types.dictionary.convert_type)


def load(file_fp: TextIO) -> Dict[Any, Any]:
    """Parse the DOTENV file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.env", "r") as dotenv_file:
    ...     load(dotenv_file)
    {'DB_DB2_HOST': 'localhost', 'DB_DB2_PORT': 50000, ...}
    """

    return loads(file_fp.read())
