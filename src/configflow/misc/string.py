"""Module for the string helper functions and primitive data types."""

from __future__ import annotations

import warnings

from ast import literal_eval
from typing import Any
from typing import Optional

from apm import case
from apm import InstanceOf


# WPS600 - inheritance from the str is the only way to implement correct
# error message with all str functionality
class ErrorMessage(str):  # noqa: WPS600
    """Implementation of the error message.

    Notes
    -----
    By default, error messages in the exceptions don't support line breaks
    or any formatting, this decorator is solving that problem.

    References
    ----------
    1. `New line on error message in KeyError - Python 3.3 <https://stackoverflow.com/questions/
    46892261/new-line-on-error-message-in-keyerror-python-3-3>`_
    """

    def __repr__(self) -> str:
        r"""Get object representation.

        Examples
        --------
        >>> msg = ErrorMessage("\nInvalid argument: 'db'.\nExpected arguments: ['db2', 'port'].")
        >>> repr(msg)
        \nInvalid argument: 'db'.\nExpected arguments: ['db2', 'port'].
        >>> raise ValueError(msg)
        Traceback (most recent call last):
        ...
        ValueError:
        Invalid argument: 'db'.
        Expected arguments: ['db2', 'port'].
        """

        return self.__str__()


# WPS110 - in this context value is an abstract name
def parse(value: str) -> Optional[Any]:  # noqa: WPS110
    """Parse a string value to the appropriate Python object.

    Notes
    -----
    If a value is a sequence ``list | tuple | set`` then ``parse`` function will be applied
    to each element of a sequence.

    Warnings
    --------
    Currently ``parse`` function supports only primitive data types ``int | str | float``
    and sequences ``list | tuple | set``. Sequences such as ``dict`` will be returned as they are
    without parsing their inner values.

    Examples
    --------
    >>> parse("1.2")
    1.2
    >>> parse("(1, 2, '3')")
    (1, 2, 3)
    >>> parse("['85', '0.23', 'cleffa', ['10', ['0.123'], 'blipbug']]")
    [85, 0.23, 'cleffa', [10, [0.123], 'blipbug']]
    """

    try:
        literal = literal_eval(value)

    except ValueError:
        original_type = type(value)
        return (
            case(value)
            .of(InstanceOf(list, set, tuple), lambda _: original_type(map(parse, value)))
            .otherwise(lambda _: value)
        )

    except SyntaxError as exception:
        warnings.warn(
            message="Error during object parsing {0!r}. Suppressed exception {1!s}.".format(
                value,
                exception,
            ),
            category=UserWarning,
        )
        return None

    original_type = type(literal)
    return (
        case(literal)
        .of(InstanceOf(float), lambda _: int(literal) if literal.is_integer() else literal)
        .of(InstanceOf(list, set, tuple), lambda _: original_type(map(parse, literal)))
        .otherwise(lambda _: literal)
    )
