"""Module for the exceptions that relate to the IO functionality."""

from __future__ import annotations

from pathlib import Path
from typing import Type

from configflow import io
from configflow import misc


class InvalidFileTypeError(Exception):
    """Raises if a file has the unsupported type."""

    def __init__(self, filepath: Path, supported_types: Type[io.enums.FileType]) -> None:
        """Initialize.

        Examples
        --------
        >>> raise InvalidFileTypeError(
        ...     filepath=Path("example.conf"),
        ...     supported_types=io.enums.FileType,
        ... )
        Traceback (most recent call last):
        ...
        configflow.exceptions.io.InvalidFileTypeError: ...
        """

        msg = misc.string.ErrorMessage("File {0!r} has invalid type. Supported types:\n{1!s}")
        fmt_supported_types = "\n".join(
            map(lambda s_type: "- {0!s}".format(s_type.name), supported_types),  # type: ignore
        )

        super().__init__(msg.format(filepath.as_posix(), fmt_supported_types))
