"""Module for the abstract configuration source and its loader."""

from __future__ import annotations

import typing
import dataclasses


DictType = typing.Dict[str, typing.Any]


@dataclasses.dataclass
class Source(object):
    """An abstract source of a configuration."""

    @property
    def content(self) -> DictType:
        """Get content of a source."""

        raise NotImplementedError

    def __repr__(self) -> str:
        """Get object representation."""

        fields = tuple(self.__dict__.items())

        signature_parts = ("{0!s}={1!r}".format(*pair) for pair in fields)
        signature = ", ".join(signature_parts)

        return "{0!s}({1!s})".format(self.__class__.__name__, signature)

    def __str__(self) -> str:
        """Get string representation."""

        return self.__repr__()
