"""Module for the abstract configuration source and its loader."""

from __future__ import annotations

from typing import Any
from typing import Dict

import pydantic


class Source(pydantic.BaseModel):
    """An abstract source of a configuration."""

    @property
    def content(self) -> Dict[str, Any]:
        """Get content of a source.

        Examples
        --------
        >>> Source().content
        Traceback (most recent call last):
        ...
        NotImplementedError
        """

        raise NotImplementedError
