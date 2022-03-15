"""Module for the file configuration source."""

from __future__ import annotations

import os
import sys

from pathlib import Path
from typing import Any
from typing import Dict
from typing import Literal
from typing import Optional

from configflow import exceptions
from configflow import io
from configflow import misc
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
        A character will be used as a level hint during the dictionary parsing, by default ``.``.
    """

    path: Optional[Path] = None
    environment_variable: Optional[str] = None
    command_line_argument: Optional[str] = None
    separator: Literal[".", "_"] = "."

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

    @property
    def content(self) -> Dict[str, Any]:
        """Get content of a source.

        Examples
        --------
        >>> source = FileSource(path=Path("tests/fixtures/example.yaml"))
        >>> source.content
        {'databases': ...}
        """

        loader = io.loader.get_loader(self.filepath)

        with open(self.filepath, "r") as file_fp:
            file_content = loader(file_fp)

        file_content = misc.dictionary.make_flat(file_content, separator=self.separator)
        return misc.dictionary.make_nested(file_content, separator=self.separator)
