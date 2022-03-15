"""Module for the exceptions that relate to the metaclass."""

from __future__ import annotations

from configflow import misc


class AttributesError(Exception):
    """Raises if arguments were passed in ``__init__`` when ``source`` was also provided."""

    def __init__(self) -> None:
        """Initialize.

        Examples
        --------
        >>> raise AttributesError()
        Traceback (most recent call last):
        ...
        configflow.exceptions.metaclass.AttributesError: ...
        """

        msg = misc.string.ErrorMessage("Provided both 'Config.source' and keyword arguments.")
        super().__init__(msg)
