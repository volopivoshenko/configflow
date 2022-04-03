"""Module for the ``DOTENV`` IO functions.

This module is a decorator of the ``python-dotenv`` package,
because it doesn't provide a common Python IO interface ``load | loads``.
"""

from __future__ import annotations

import io
import typing

import dotenv


DictType = typing.Dict[str, typing.Any]


def loads(stream: str) -> DictType:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> dotenv_stream = "DB_HOST=localhost\nDB_PORT=8080"
    >>> loads(dotenv_stream)
    {'DB_HOST': 'localhost', 'DB_PORT': '8080'}
    """

    return dict(dotenv.dotenv_values(stream=io.StringIO(stream)))


def load(file_fp: typing.TextIO) -> DictType:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.env", "r") as dotenv_file:
    ...     load(dotenv_file)
    {'DATABASES.POSTGRES.USER': 'admin', 'DATABASES.POSTGRES.PASSWORD': 'admin', ...}
    """

    return loads(file_fp.read())
