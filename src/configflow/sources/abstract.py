"""Module for the abstract configuration source and its loader."""

from __future__ import annotations

import typing
import dataclasses


DictType = typing.Dict[str, typing.Any]


@dataclasses.dataclass
class Source:
    """An abstract source of a configuration."""

    @property
    def content(self) -> DictType:
        """Get content of a source."""

        raise NotImplementedError
