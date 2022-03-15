"""Module for the ``INI`` IO functions.

This module is a decorator of the ``configparser`` package, because it doesn't provide
a common Python IO interface: ``load | loads`` and doesn't convert data types.
"""

from __future__ import annotations

import configparser

from typing import Any
from typing import Dict
from typing import TextIO

from configflow import misc


def loads(stream: str) -> Dict[str, Any]:
    r"""Parse the ``INI`` stream and produce the corresponding Python object.

    Examples
    --------
    >>> ini_stream = "\n[db.db2]\nhost = localhost\nport = 50000"
    >>> loads(ini_stream)
    {'db.db2': {'host': 'localhost', 'port': 50000}}
    """

    parser = configparser.ConfigParser()
    parser.read_string(stream)
    # noinspection PyProtectedMember
    parsed_values = dict(parser._sections)  # type: ignore
    # TODO Remove parsing of the values as it will be handle by pydantic
    return misc.dictionary.deep_map(misc.string.parse, parsed_values)


def load(file_fp: TextIO) -> Dict[str, Any]:
    """Parse the ``INI`` file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.ini", "r") as ini_file:
    ...     load(ini_file)
    {'databases.postgres': {'user': 'admin', ...}, ...}
    """

    return loads(file_fp.read())
