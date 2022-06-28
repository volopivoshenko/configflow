"""Module for the ``YAML`` IO functions."""

from __future__ import annotations

import typing

from configflow import misc


try:
    import yaml

except ImportError:
    yaml = None  # type: ignore[assignment]


DictType = typing.Dict[str, typing.Any]


@misc.decorators.external(dependency=yaml, pypi="pyyaml")  # type: ignore[call-arg]
def loads(stream: str) -> DictType:
    """Parse the stream and produce the corresponding Python object.

    Examples
    --------
    >>> dotenv_stream = "databases: localhost"
    >>> loads(dotenv_stream)
    {'databases': 'localhost'}
    """

    return yaml.safe_load(stream)


def load(file_fp: typing.TextIO) -> DictType:
    """Parse the file in a stream and produce the corresponding Python object.

    Examples
    --------
    >>> with open("tests/fixtures/example.yaml", "r") as yaml_file:
    ...     load(yaml_file)
    {'databases': {...}, ...}
    """

    return loads(file_fp.read())
