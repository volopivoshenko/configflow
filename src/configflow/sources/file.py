"""Module for the file configuration source."""

from __future__ import annotations

import os
import sys
import typing
import pathlib

import typing_extensions

from configflow import exceptions
from configflow import io
from configflow import misc
from configflow import sources


DictType = typing.Dict[str, typing.Any]
PathType = typing.Optional[typing.Union[str, pathlib.Path]]


class FileSource(sources.abstract.Source):
    """File as a source of a configuration.

    Attributes
    ----------
    path : PathType
        Path to the configuration file, by default ``None``.

    environment_variable : typing.Optional[str]
        Name of the OS environment variable that contains the path to the configuration file,
        e.g. ``DEV_CONFIG``. It's alternative of the ``path`` attribute, by default ``None``.

    command_line_argument : typing.Optional[str]
        Name of the command-line argument that contains the path to the configuration file,
        e.g. ``-c | --config``. It's alternative of the ``path`` attribute, by default ``None``.

    separator : typing_extensions.Literal[".", "_"]
        A character will be used as a level hint during the dictionary parsing, by default ``.``.
    """

    path: PathType = None
    environment_variable: typing.Optional[str] = None
    command_line_argument: typing.Optional[str] = None
    separator: typing_extensions.Literal[".", "_"] = "."

    @property
    def filepath(self) -> pathlib.Path:
        """Get a path to a configuration file.

        Raises
        ------
        CommandLineArgumentError
            If a command-line argument doesn't have a value.

        SourceError
            If a source doesn't have a filepath.

        Examples
        --------
        >>> source = FileSource(path=pathlib.Path("tests/fixtures/example.env"))
        >>> source.filepath.as_posix()
        tests/fixtures/example.env
        """

        filepath: pathlib.Path

        if self.path:
            filepath = pathlib.Path(self.path)

        elif self.environment_variable:
            filepath = pathlib.Path(os.getenv(self.environment_variable, ""))

        elif self.command_line_argument:
            try:
                index = sys.argv.index(self.command_line_argument)

            except ValueError:
                raise exceptions.sources.CommandLineArgumentError(
                    msg="Argument {0!r} doesn't not exist.",
                    command_line_argument=self.command_line_argument,
                )

            try:
                filepath = pathlib.Path(sys.argv[index + 1])

            except IndexError:
                raise exceptions.sources.CommandLineArgumentError(
                    msg="Argument {0!r} doesn't have value.",
                    command_line_argument=self.command_line_argument,
                )

        else:
            raise exceptions.sources.SourceError(
                msg="Configuration filepath is not set.",
                source=self,
            )

        return filepath

    @property
    def content(self) -> DictType:
        """Get content of a source.

        Examples
        --------
        >>> source = FileSource(path=pathlib.Path("tests/fixtures/example.yaml"))
        >>> source.content
        {'databases': ...}
        """

        loader = io.loader.get_loader(self.filepath)

        with open(self.filepath, "r") as file_fp:
            file_content = loader(file_fp)

        file_content = misc.dictionary.make_flat(file_content, separator=self.separator)
        return misc.dictionary.make_nested(file_content, separator=self.separator)
