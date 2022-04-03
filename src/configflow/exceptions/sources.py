"""Module for the exceptions that relate to the configuration sources."""

from __future__ import annotations

from configflow import misc
from configflow.sources import abstract


class CommandLineArgumentError(Exception):
    """Raises if the user passed an invalid command-line argument."""

    def __init__(self, msg: str, command_line_argument: str) -> None:
        """Initialize.

        Examples
        --------
        >>> raise CommandLineArgumentError(
        ...     msg="Argument {0!r} doesn't have value.",
        ...     command_line_argument="-c"
        ... )
        Traceback (most recent call last):
        ...
        configflow.exceptions.sources.CommandLineArgumentError: ...
        """

        super().__init__(misc.string.ErrorMessage(msg).format(command_line_argument))


class SourceError(Exception):
    """Raises if the user passed an invalid source of a configuration."""

    def __init__(self, source: abstract.Source, msg: str) -> None:
        """Initialize.

        Examples
        --------
        >>> raise SourceError(abstract.Source(), "Filepath is not set.")
        Traceback (most recent call last):
        ...
        configflow.exceptions.sources.SourceError: ...
        """

        super().__init__(misc.string.ErrorMessage("{0!s}. Source:\n{1!r}").format(msg, source))
