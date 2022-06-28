"""Module for the ``YAML`` IO functions."""

from __future__ import annotations

import typing

from configflow import misc


# WPS440, WPS443 - nested import is necessary for the modular package dependencies
try:
    import yaml  # noqa: WPS443

except ImportError:
    yaml = None  # noqa: WPS440


DictType = typing.Dict[str, typing.Any]


@misc.decorators.external(dependency=yaml, pypi="pyyaml")
def loads(stream: str) -> DictType:
    r"""Parse the stream and produce the corresponding Python object.

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
