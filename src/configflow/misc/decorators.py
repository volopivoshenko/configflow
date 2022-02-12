"""Module for the decorators."""

from __future__ import annotations

import warnings

from typing import Any
from typing import Callable

import decorator


@decorator.decorator
def deprecated(function: Callable[[Any], Any], *args, **kwargs) -> Any:
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

    warnings.warn("Function {0!r} is deprecated.".format(function.__name__), DeprecationWarning)
    return function(*args, **kwargs)
