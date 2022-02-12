"""Module for the factory that returns a load functions on a file type."""

from __future__ import annotations

import json

from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import TextIO

import apm
import toml
import yaml

from configflow import exceptions
from configflow import io


def get_loader(filename: Path) -> Callable[[TextIO], Dict[str, Any]]:
    """Get a load function based on a file type.

    Raises
    ------
    InvalidFileTypeError
        If a file has the unsupported type.

    Examples
    --------
    >>> get_loader(Path(".env"))
    <function load at ...>
    """

    # WPS472 - in this case is prettier than direct indexing
    *_, suffix = filename.as_posix().split(".")  # noqa: WPS472

    try:
        file_type = io.enums.FileType[suffix]

    except KeyError:
        raise exceptions.io.InvalidFileTypeError(filename, io.enums.FileType)

    return (
        apm.case(file_type)
        .of(apm.OneOf(io.enums.FileType.yaml, io.enums.FileType.yml), lambda _: yaml.safe_load)
        .of(apm.OneOf(io.enums.FileType.ini, io.enums.FileType.cfg), lambda _: io.ini.load)
        .of(io.enums.FileType.json, lambda _: json.load)
        .of(io.enums.FileType.toml, lambda _: toml.load)
        .of(io.enums.FileType.env, lambda _: io.dotenv.load)
        .otherwise(lambda _: yaml.load)
    )
