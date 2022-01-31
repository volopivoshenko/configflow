"""Module for the dictionary helper functions."""

from __future__ import annotations

import copy

from typing import Any
from typing import Callable
from typing import Dict

import apm


def deep_map(
    function: Callable[[Any], Any],
    dictionary: Dict[str, Any],
) -> Dict[str, Any]:
    """Apply a function to the values of a dictionary.

    Notes
    -----
    If a value is a sequence ``list | set | tuple`` then a function will be applied
    to each element of a sequence.

    Warnings
    --------
    If a sequence contains another sequence then a function won't be applied to each
    element of a sequence, as long as the passed function doesn't deal with sequences.

    Examples
    --------
    >>> import functools
    >>> ports = {
    ...     "db": {
    ...         "db2": 50000,
    ...         "postgres": 5432,
    ...         "mongo": {
    ...             "v1": [8000, 5000],
    ...         }
    ...     },
    ...     "hub": 8080,
    ... }
    >>> deep_map(lambda port: port + 1, ports)
    {'db': {'db2': 50001, 'postgres': 5433, 'mongo': {'v1': [8001, 5001]}}, 'hub': 8081}
    >>> func_with_mul_args = functools.partial(lambda inc, port: port + inc, 5)
    >>> deep_map(func_with_mul_args, ports)
    {'db': {'db2': 50005, 'postgres': 5437, 'mongo': {'v1': [8005, 5005]}}, 'hub': 8085}
    """

    original_type = type(dictionary)

    # WPS110 - in this context value is a dummy and abstract name
    return (
        apm.case(dictionary)
        .of(
            apm.InstanceOf(dict),
            lambda _: {
                key: deep_map(function, value) for key, value in dictionary.items()  # noqa: WPS110
            },
        )
        .of(apm.InstanceOf(list, set, tuple), lambda _: original_type(map(function, dictionary)))
        .otherwise(lambda _: function(dictionary))
    )


def update(to_dictionary: Dict[str, Any], from_dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """Update values of a dictionary based on another dictionary.

    Examples
    --------
    >>> to_dict = {
    ... "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
    ... "hub": {"env": "prod", "auth": "basic"},
    ... "timeout": 10,
    ... }
    >>> from_dict = {
    ... "db": {"host": "localhost", "ports": {"v1": 8000, "v2": 5000, "v3": 80}},
    ... "hub": {"env": "dev"},
    ... "warnings": "suppress",
    ... "timeout": 10,
    ... }
    >>> update(to_dict, from_dict)
    {'db': {'host': 'localhost', 'ports': {'v1': 8000, 'v2': 5000, 'v3': 80}},
     'hub': {'env': 'dev', 'auth': 'basic'}, 'timeout': 10, 'warnings': 'suppress'}
    """

    upd_dictionary = copy.deepcopy(to_dictionary)

    # WPS110 - in this context value is a dummy and abstract name
    for key, value in from_dictionary.items():  # noqa: WPS110
        upd_dictionary[key] = (
            update(to_dictionary.get(key, {}), value)
            if isinstance(value, dict)
            else from_dictionary[key]
        )

    return upd_dictionary
