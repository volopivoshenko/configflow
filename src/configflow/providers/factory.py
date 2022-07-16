"""Module for the factory that returns an IO provider based on a file type."""

from __future__ import annotations

import enum
import json
import types
import pathlib

import apm

from configflow import exceptions
from configflow import providers


DependencyType = types.ModuleType


# WPS600 - inheritance from the str is the only way to implement correct behavior
# noinspection PyArgumentList
class FileType(str, enum.Enum):  # noqa: WPS600
    """Supported file types."""

    yaml: int = enum.auto()
    yml: int = enum.auto()
    ini: int = enum.auto()
    cfg: int = enum.auto()
    conf: int = enum.auto()
    config: int = enum.auto()
    json: int = enum.auto()
    toml: int = enum.auto()
    env: int = enum.auto()
    properties: int = enum.auto()


def get_provider(filepath: pathlib.Path) -> DependencyType:
    """Get a IO provider based on a file type.

    Raises
    ------
    FileTypeError
        If a file has the unsupported type.

    Examples
    --------
    >>> get_provider(pathlib.Path(".env"))
    <module 'configflow.providers.dotenv' from ...>
    """

    suffix = filepath.as_posix().split(".")[-1]

    try:
        file_type = FileType[suffix]

    except KeyError:
        raise exceptions.providers.FileTypeError(filepath, FileType)

    return (
        apm.case(file_type)  # noqa: WPS221
        .of(FileType.json, lambda _: json)
        .of(FileType.toml, lambda _: providers.toml)
        .of(FileType.env, lambda _: providers.dotenv)
        .of(FileType.properties, lambda _: providers.properties)
        .of(apm.OneOf(FileType.yaml, FileType.yml), lambda _: providers.yaml)
        .of(apm.OneOf(FileType.ini, FileType.cfg, FileType.conf), lambda _: providers.ini)
        .otherwise(lambda _: providers.ini)
    )
