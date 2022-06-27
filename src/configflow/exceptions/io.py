"""Module for the exceptions that relate to the IO functionality."""

from __future__ import annotations

import typing
import pathlib

from configflow import misc
from configflow import providers


class FileTypeError(Exception):
    """Raises if a file has the unsupported type."""

    def __init__(
        self,
        filepath: pathlib.Path,
        supported_types: typing.Type[providers.loader.FileType],
    ) -> None:
        """Initialize.

        Examples
        --------
        >>> raise FileTypeError(
        ...     filepath=pathlib.Path("example.conf"),
        ...     supported_types=providers.loader.FileType,
        ... )
        Traceback (most recent call last):
        ...
        configflow.exceptions.io.FileTypeError: ...
        """

        msg = misc.string.ErrorMessage("File {0!r} has invalid type. Supported types:\n{1!s}")
        fmt_supported_types = "\n".join(
            ("- {0!s}".format(s_type.name) for s_type in supported_types),  # type: ignore
        )

        super().__init__(msg.format(filepath.as_posix(), fmt_supported_types))
