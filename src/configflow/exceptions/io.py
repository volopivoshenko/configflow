"""Exceptions that relate to the IO functionality."""

from __future__ import annotations

import json

from pathlib import Path
from typing import Type

from configflow.io import enums
from configflow.types import error


class InvalidFileTypeError(Exception):
    """Raises if a file has the unsupported type."""

    def __init__(self, filepath: Path, supported_types: Type[enums.FileType]) -> None:
        """Initialize."""

        msg = error.ErrorMessage("File {0!r} has invalid type. Supported types:\n{1!s}.")
        fmt_supported_types = json.dumps([f_type.name for f_type in supported_types], indent=2)
        super().__init__(msg.format(filepath.as_posix(), fmt_supported_types))
