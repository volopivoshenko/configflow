"""An abstract source of the configuration."""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass
class Source(ABC):
    """An abstract source of the configuration."""


class SourceLoader(ABC):
    """An abstract loader of the configuration source."""
