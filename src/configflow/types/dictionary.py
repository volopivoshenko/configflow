"""Dictionary helper functions."""

from __future__ import annotations

from ast import literal_eval
from typing import Any
from typing import Callable
from typing import Dict

from apm import case
from apm import InstanceOf


def deep_map(
    dictionary: Dict[Any, Any],
    function: Callable[[Any], Any],
) -> Dict[Any, Any]:
    """Apply function to the values of the nested dictionary.

    Examples
    --------
    >>> values = {
    ...     "vectors": {
    ...         "vec_a": {"x": 1, "y": 2},
    ...         "vec_b": {"x": 0, "y": 0},
    ...     },
    ... }
    >>> deep_map(values, lambda arg: arg + 1)
    {'vectors': {'vec_a': {'x': 2, 'y': 3}, 'vec_b': {'x': 1, 'y': 1}}}
    """

    # WPS110 - in this context value is a dummy and abstract name
    return (
        {key: deep_map(value, function) for key, value in dictionary.items()}  # noqa: WPS110
        if isinstance(dictionary, dict)
        else function(dictionary)
    )


def convert_type(raw_value: str) -> Any:
    """Convert string value to the appropriate Python data type.

    Examples
    --------
    >>> convert_type("1")
    1
    >>> convert_type("1.2")
    1.2
    >>> convert_type("string")
    'string'
    >>> convert_type("(1, 2, 3)")
    (1, 2, 3)
    """

    try:
        literal = literal_eval(raw_value)

    except ValueError:
        return raw_value

    except SyntaxError:
        return None

    sequence_type = (
        case(literal)
        .of(InstanceOf(list), lambda _: list)
        .of(InstanceOf(set), lambda _: set)
        .of(InstanceOf(tuple), lambda _: tuple)
        .otherwise(lambda _: list)
    )

    return (
        case(literal)
        .of(InstanceOf(float), lambda _: int(literal) if literal.is_integer() else literal)
        .of(InstanceOf(list, set, tuple), lambda _: sequence_type(map(convert_type, literal)))
        .otherwise(lambda _: literal)
    )
