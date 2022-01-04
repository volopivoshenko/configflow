"""The factory that returns the IO module based on the file extension."""

from __future__ import annotations

import json

from pathlib import Path
from types import ModuleType

import toml
import yaml

from apm import case
from apm import OneOf

from configflow import exceptions
from configflow.io import dotenv
from configflow.io import enums
from configflow.io import ini


class IOFactory(object):
    """The factory that returns IO module based on the file extension."""

    def __getitem__(self, filename: Path) -> ModuleType:
        """Get IO module based on file type.

        Raises
        ------
        InvalidFileTypeError
            If a file has the unsupported type.

        Examples
        --------
        >>> io_factory = IOFactory()
        >>> io_factory[Path("example.json")]
        <module 'json' ...>
        """

        suffix = filename.suffix.strip(".")

        try:
            extension = enums.FileType[suffix]

        except KeyError:
            raise exceptions.io.InvalidFileTypeError(filename, enums.FileType)

        # noinspection PyTypeChecker
        return (
            case(extension)
            .of(OneOf(enums.FileType.yaml, enums.FileType.yml), lambda _: yaml)
            .of(OneOf(enums.FileType.ini, enums.FileType.cfg), lambda _: ini)
            .of(enums.FileType.json, lambda _: json)
            .of(enums.FileType.toml, lambda _: toml)
            .of(enums.FileType.env, lambda _: dotenv)
            .otherwise(lambda _: yaml)
        )

    def get(self, filename: Path) -> ModuleType:
        """Get IO module based on file type.

        Examples
        --------
        >>> io_factory = IOFactory()
        >>> io_factory.get(Path("example.env"))
        <module 'configflow.io.dotenv' ...>
        """

        return self.__getitem__(filename)
