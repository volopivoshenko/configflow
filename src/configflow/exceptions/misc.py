"""Module for the exceptions that relate to the utility functionality."""

from __future__ import annotations

import json
import typing

from configflow import misc


class EmptyKeyError(Exception):
    """Raises if a dictionary contains an empty key."""

    def __init__(self, dictionary: typing.Dict[str, typing.Any]) -> None:
        """Initialize.

        Examples
        --------
        >>> raise EmptyKeyError(dictionary={"db__postgres": {"host": "localhost"}})
        Traceback (most recent call last):
        ...
        configflow.exceptions.misc.EmptyKeyError: ...
        """

        msg = misc.string.ErrorMessage("Got an empty key. Dictionary\n{0!s}")
        fmt_dictionary = json.dumps(dictionary, indent=2)

        super().__init__(msg.format(fmt_dictionary))


class DuplicatedKeyError(Exception):
    """Raises if a dictionary contains a duplicated key."""

    def __init__(self, key: str, dictionary: typing.Dict[str, typing.Any]) -> None:
        """Initialize.

        Examples
        --------
        >>> raise DuplicatedKeyError(
        ...     key="postgres",
        ...     dictionary={"db_postgres": {"port": "80"}, "db_postgres_port": 80},
        ... )
        Traceback (most recent call last):
        ...
        configflow.exceptions.misc.DuplicatedKeyError: ...
        """

        msg = misc.string.ErrorMessage("Key {0!r} is already presented. Dictionary\n{1!s}")
        fmt_dictionary = json.dumps(dictionary, indent=2)

        super().__init__(msg.format(key, fmt_dictionary))
