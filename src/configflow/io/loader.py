"""Module for the factory that returns the IO module based on a file type."""

from __future__ import annotations

import json

from pathlib import Path
from types import ModuleType

import apm
import toml
import yaml

from configflow import exceptions
from configflow import io


def get_io_module(filename: Path) -> ModuleType:
    """Get IO module based on a file type.

    Raises
    ------
    InvalidFileTypeError
        If a file has the unsupported type.

    Examples
    --------
    >>> get_io_module(Path(".env"))
    <module 'configflow.io.dotenv' from ...>
    """

    # WPS472 - in this case is prettier than direct indexing
    *_, suffix = filename.as_posix().split(".")  # noqa: WPS472

    try:
        file_type = io.enums.FileType[suffix]

    except KeyError:
        raise exceptions.io.InvalidFileTypeError(filename, io.enums.FileType)

    return (
        apm.case(file_type)
        .of(apm.OneOf(io.enums.FileType.yaml, io.enums.FileType.yml), lambda _: yaml)
        .of(apm.OneOf(io.enums.FileType.ini, io.enums.FileType.cfg), lambda _: io.ini)
        .of(io.enums.FileType.json, lambda _: json)
        .of(io.enums.FileType.toml, lambda _: toml)
        .of(io.enums.FileType.env, lambda _: io.dotenv)
        .otherwise(lambda _: yaml)
    )
