"""Module for the ``TOML`` IO functions."""

from __future__ import annotations

import typing

from configflow import misc


try:
    import toml

except ImportError:
    toml = None  # type: ignore[assignment]


DictType = typing.Dict[str, typing.Any]


@misc.decorators.external(dependency=toml, pypi="toml")  # type: ignore[call-arg]
def loads(stream: str) -> DictType:
    r"""Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> dotenv_stream = "[databases.postgres]\nuser = 'admin'"
    >>> loads(dotenv_stream)
    {'databases': {'postgres': {'user': 'admin'}}}
    """

    return toml.loads(stream)


def load(file_fp: typing.TextIO) -> DictType:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.toml", "r") as yaml_file:
    ...     load(yaml_file)
    {'databases': {...}, ...}
    """

    return loads(file_fp.read())
