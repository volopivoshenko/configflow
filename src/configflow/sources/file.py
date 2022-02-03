"""Module for the file configuration source and its loader."""

from __future__ import annotations

import os
import sys

from pathlib import Path
from typing import Literal
from typing import Optional

from configflow import exceptions
from configflow import sources


class FileSource(sources.abstract.Source):
    """File as a source of a configuration.

    Attributes
    ----------
    path : Optional[Path]
        Path to the configuration file, by default ``None``.

    environment_variable : Optional[str]
        Name of the OS environment variable that contains the path to the configuration file,
        e.g. ``DEV_CONFIG``. It's alternative of the ``path`` attribute, by default ``None``.

    command_line_argument : Optional[str]
        Name of the command-line argument that contains the path to the configuration file,
        e.g. ``-c | --config``. It's alternative of the ``path`` attribute, by default ``None``.

    separator : Literal[".", "_"]
        A character will be used as a level hint during the dictionary parsing, by default ``_``.
    """

    path: Optional[Path] = None
    environment_variable: Optional[str] = None
    command_line_argument: Optional[str] = None
    separator: Literal[".", "_"] = "_"

    @property
    def filepath(self) -> Path:
        """Get a path to a configuration file.

        Raises
        ------
        CommandLineArgumentError
            If a command-line argument doesn't have a value.

        InvalidSourceError
            If a source doesn't have filepath.

        Examples
        --------
        >>> source = FileSource(path=Path("tests/fixtures/example.env"))
        >>> source.filepath
        PosixPath('tests/fixtures/example.env')
        """

        filepath: Path

        if self.path:
            filepath = self.path

        elif self.environment_variable and os.getenv(self.environment_variable):
            filepath = Path(os.getenv(self.environment_variable, ""))

        elif self.command_line_argument and self.command_line_argument in sys.argv:
            index = sys.argv.index(self.command_line_argument)

            try:
                filepath = Path(sys.argv[index + 1])

            except IndexError:
                raise exceptions.sources.CommandLineArgumentError(self.command_line_argument)

        else:
            raise exceptions.sources.InvalidSourceError(
                msg="Configuration filepath is not set.",
                source=self,
            )

        return filepath
