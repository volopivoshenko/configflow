"""Module for the enums."""

from __future__ import annotations

import enum

from typing import Iterator


class FileType(enum.Enum):
    """Supported file types.

    - ``YAML | .yaml``
    - ``YML | .yml``
    - ``INI | .ini``
    - ``CFG | .cfg``
    - ``JSON | .json``
    - ``TOML | .toml``
    - ``ENV | .env``
    """

    yaml: int = enum.auto()
    yml: int = enum.auto()
    ini: int = enum.auto()
    cfg: int = enum.auto()
    json: int = enum.auto()
    toml: int = enum.auto()
    env: int = enum.auto()

    def __str__(self) -> str:
        """Get string representation."""

        return self.name

    def __iter__(self) -> Iterator[FileType]:
        """Get iterator.

        Notes
        -----
        Implementation of the ``__iter__`` method is required
        for the ``mypy`` correct linting.
        """

        return self.__iter__()
