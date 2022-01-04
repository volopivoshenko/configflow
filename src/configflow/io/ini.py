"""Implementation of the INI IO functions.

This module is a decorator of the ``configparser`` package, because it
doesn't provide common Python IO interface: ``load | loads`` and doesn't
convert data types.
"""

from __future__ import annotations

import configparser

from typing import Any
from typing import Dict
from typing import TextIO

from configflow import types


def loads(stream: str) -> Dict[Any, Any]:
    r"""Parse the INI stream and produce the corresponding Python object.

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
    return types.dictionary.deep_map(parsed_values, types.dictionary.convert_type)


def load(file_fp: TextIO) -> Dict[Any, Any]:
    """Parse the INI file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.ini", "r") as ini_file:
    ...     load(ini_file)
    {'db.db2': {'host': 'localhost', ...}, ...}
    """

    return loads(file_fp.read())
