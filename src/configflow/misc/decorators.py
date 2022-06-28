"""Module for the decorators."""

from __future__ import annotations

import types
import typing
import warnings

import decorator

from configflow import misc


FunctionType = typing.Callable[[typing.Any], typing.Any]
DependencyType = typing.Optional[types.ModuleType]


@decorator.decorator
def deprecated(function: FunctionType, *args, **kwargs) -> typing.Any:
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


@decorator.decorator
def external(
    function: FunctionType,
    dependency: DependencyType = None,
    pypi: typing.Optional[str] = None,
    *args,
    **kwargs,
) -> typing.Any:
    """Check if the external dependency is installed.

    Examples
    --------
    >>> @external(dependency=None, pypi="hvac")
    >>> def logger(handler: str, filters: list) -> None:
    ...     print("Logger is ready.")
    >>> logger(..., ...)
    Traceback (most recent call last):
    ...
    ImportError: 'hvac' is not installed. Please install it with `poetry add configflow[hvac]`.
    """

    if dependency:
        return function(*args, **kwargs)

    msg = misc.string.ErrorMessage(
        "{0!r} is not installed. Please install it with `poetry add configflow[{0!s}]`.",
    )
    raise ImportError(msg.format(pypi))
