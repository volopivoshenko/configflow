"""Module for the abstract configuration source and its loader."""

from __future__ import annotations

import abc

from typing import Any
from typing import Dict

import pydantic


class Source(pydantic.BaseModel):
    """An abstract source of a configuration."""


class SourceLoader(abc.ABC):
    """An abstract loader of a configuration source."""

    def __init__(self, source: Source) -> None:
        """Initialize."""

        self._source = source

    @abc.abstractmethod
    def source_content(self) -> Dict[str, Any]:
        """Get content of a source."""

        raise NotImplementedError
