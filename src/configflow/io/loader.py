"""Module for the factory that returns a load functions on a file type."""

from __future__ import annotations

import enum
import json
import typing
import pathlib

import apm
import toml
import yaml

from configflow import exceptions
from configflow import io


LoaderType = typing.Callable[[typing.TextIO], typing.Dict[str, typing.Any]]


class FileType(enum.Enum):
    """Supported file types."""

    yaml: int = enum.auto()
    yml: int = enum.auto()
    ini: int = enum.auto()
    cfg: int = enum.auto()
    config: int = enum.auto()
    json: int = enum.auto()
    toml: int = enum.auto()
    env: int = enum.auto()

    def __str__(self) -> str:
        """Get string representation.

        Examples
        --------
        >>> str(FileType.yaml)
        yaml
        """

        return self.name


def get_loader(filepath: pathlib.Path) -> LoaderType:
    """Get a load function based on a file type.

    Raises
    ------
    FileTypeError
        If a file has the unsupported type.

    Examples
    --------
    >>> get_loader(pathlib.Path(".env"))
    <function load at ...>
    """

    suffix = filepath.as_posix().split(".")[-1]

    try:
        file_type = FileType[suffix]

    except KeyError:
        raise exceptions.io.FileTypeError(filepath, FileType)

    return (
        apm.case(file_type)
        .of(apm.OneOf(FileType.yaml, FileType.yml), lambda _: yaml.safe_load)
        .of(apm.OneOf(FileType.ini, FileType.cfg), lambda _: io.ini.load)
        .of(FileType.json, lambda _: json.load)
        .of(FileType.toml, lambda _: toml.load)
        .of(FileType.env, lambda _: io.dotenv.load)
        .otherwise(lambda _: yaml.load)
    )
