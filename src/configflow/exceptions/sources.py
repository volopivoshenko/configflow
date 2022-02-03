"""Module for the exceptions that relate to the configuration sources."""

from __future__ import annotations

from configflow import misc
from configflow.sources import abstract


class CommandLineArgumentError(Exception):
    """Raises if the user passed an invalid command-line argument."""

    def __init__(self, command_line_argument: str) -> None:
        """Initialize.

        Examples
        --------
        >>> raise CommandLineArgumentError(command_line_argument="-c")
        Traceback (most recent call last):
        ...
        configflow.exceptions.sources.CommandLineArgumentError: ...
        """

        msg = misc.string.ErrorMessage("Argument {0!r} doesn't have value.")
        super().__init__(msg.format(command_line_argument))


class InvalidSourceError(Exception):
    """Raises if the user passed an invalid source of a configuration."""

    def __init__(self, source: abstract.Source, msg: str) -> None:
        """Initialize.

        Examples
        --------
        >>> raise InvalidSourceError(abstract.Source(), "Filepath is not set.")
        Traceback (most recent call last):
        ...
        configflow.exceptions.sources.InvalidSourceError: ...
        """

        super().__init__(misc.string.ErrorMessage("{0!s}. Source:\n{1!r}").format(msg, source))
