"""Module for the decorators."""

from __future__ import annotations

import typing
import warnings


FunctionType = typing.Callable[[typing.Any], typing.Any]


def deprecated(function: FunctionType) -> typing.Any:
    """Show warning about the depreciation of a function or method.

    Examples
    --------
    >>> @deprecated
    >>> def logger(handler: str, filters: list) -> None:
    ...     ...
    >>> with warnings.catch_warnings(record=True) as warning:
    ...     warnings.simplefilter("always")
    ...     logger(..., ...)
    ...     warning
    [<warnings.WarningMessage object at ...]
    """

    def wrapper(*args, **kwargs) -> typing.Any:
        """Show warning about the depreciation of a function or method."""

        warnings.warn("Function {0!r} is deprecated.".format(function.__name__), DeprecationWarning)
        return function(*args, **kwargs)

    return wrapper
