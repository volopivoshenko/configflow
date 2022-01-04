"""File as a source of the configuration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal
from typing import Optional
from typing import Union

from configflow.sources import abstract


@dataclass
class FileSource(abstract.Source):
    """File as a source of the configuration.

    Attributes
    ----------
    path : Optional[Union[str, Path]]
        Path to the configuration file, by default ``None``.

    environment_variable : Optional[str]
        Name of the OS environment variable that contains path
        to the configuration file, e.g. ``DEV_CONFIGURATION``.
        It's alternative of the ``path`` attribute, by default ``None``.

    commandline_argument : Optional[str]
        Name of the command-line argument that contains path
        to the configuration file, e.g. ``-c | --config``.
        It's alternative of the ``path`` attribute, by default ``None``.

    separator : Literal[".", "_", "__"]
        The character will be used as a level hint during the parsing
        dictionary to nested (level hint) or flat (joining levels on)
        representations, by default ``_``.
    """

    path: Optional[Union[str, Path]] = None
    environment_variable: Optional[str] = None
    commandline_argument: Optional[str] = None
    separator: Literal[".", "_", "__"] = "_"
