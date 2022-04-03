"""Module for the ``INI | CFG | CONFIG`` IO functions.

This module is a decorator of the ``configparser`` package,
because it doesn't provide a common Python IO interface: ``load | loads``.
"""

from __future__ import annotations

import typing
import configparser


DictType = typing.Dict[str, typing.Any]


def loads(stream: str) -> DictType:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> ini_stream = "\n[db.db2]\nhost = localhost\nport = 50000"
    >>> loads(ini_stream)
    {'db.db2': {'host': 'localhost', 'port': '50000'}}
    """

    parser = configparser.ConfigParser(dict_type=dict)
    parser.read_string(stream)
    # noinspection PyProtectedMember
    return dict(parser._sections)  # type: ignore


def load(file_fp: typing.TextIO) -> DictType:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.ini", "r") as ini_file:
    ...     load(ini_file)
    {'databases.postgres': {'user': 'admin', ...}, ...}
    """

    return loads(file_fp.read())
