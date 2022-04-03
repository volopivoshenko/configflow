"""Module for the abstract configuration source and its loader."""

from __future__ import annotations

import typing

import pydantic


DictType = typing.Dict[str, typing.Any]


class Source(pydantic.BaseModel):
    """An abstract source of a configuration."""

    @property
    def content(self) -> DictType:
        """Get content of a source.

        Examples
        --------
        >>> Source().content
        Traceback (most recent call last):
        ...
        NotImplementedError
        """

        raise NotImplementedError
