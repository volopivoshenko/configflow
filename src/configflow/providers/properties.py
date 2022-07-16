"""Module for the ``PROPERTIES`` IO functions.

This module is a decorator of the ``configparser`` package,
because it doesn't provide a common Python IO interface: ``load | loads``.
"""

from __future__ import annotations

import typing


DictType = typing.Dict[str, typing.Any]


def loads(stream: str) -> DictType:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> props_stream = "\ndb.mysql.host=localhost\ndb.mysql.password=admin"
    >>> loads(props_stream)
    {'db.mysql.host': 'localhost', ...}
    """

    return dict(
        line.split("=")  # type: ignore
        for line in stream.splitlines()
        if not line.startswith("#") and line
    )


def load(file_fp: typing.TextIO) -> DictType:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.properties", "r") as props_file:
    ...     load(props_file)
    {'databases.kafka.consumer.auto_offset_reset': 'earliest', ...}
    """

    return loads(file_fp.read())
