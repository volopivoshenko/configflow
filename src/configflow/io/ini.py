"""Module for the ``INI | CFG | CONFIG`` IO functions.

This module is a decorator of the ``configparser`` package,
because it doesn't provide a common Python IO interface: ``load | loads``.
"""

from __future__ import annotations

import configparser

from typing import Any
from typing import Dict
from typing import TextIO


def loads(stream: str) -> Dict[str, Any]:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> ini_stream = "\n[db.db2]\nhost = localhost\nport = 50000"
    >>> loads(ini_stream)
    {'db.db2': {'host': 'localhost', 'port': '50000'}}
    """

    parser = configparser.ConfigParser()
    parser.read_string(stream)
    # noinspection PyProtectedMember
    return dict(parser._sections)  # type: ignore


def load(file_fp: TextIO) -> Dict[str, Any]:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.ini", "r") as ini_file:
    ...     load(ini_file)
    {'databases.postgres': {'user': 'admin', ...}, ...}
    """

    return loads(file_fp.read())
