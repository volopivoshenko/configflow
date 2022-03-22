"""Module for the ``DOTENV`` IO functions.

This module is a decorator of the ``python-dotenv`` package,
because it doesn't provide a common Python IO interface ``load | loads``.
"""

from __future__ import annotations

from io import StringIO
from typing import Any
from typing import Dict
from typing import TextIO

from dotenv import dotenv_values


def loads(stream: str) -> Dict[str, Any]:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> dotenv_stream = "DB_HOST=localhost\nDB_PORT=8080"
    >>> loads(dotenv_stream)
    {'DB_HOST': 'localhost', 'DB_PORT': '8080'}
    """

    return dict(dotenv_values(stream=StringIO(stream)))


def load(file_fp: TextIO) -> Dict[str, Any]:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.env", "r") as dotenv_file:
    ...     load(dotenv_file)
    {'DATABASES.POSTGRES.USER': 'admin', 'DATABASES.POSTGRES.PASSWORD': 'admin', ...}
    """

    return loads(file_fp.read())
