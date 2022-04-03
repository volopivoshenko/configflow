"""Module for the dictionary helper functions."""

from __future__ import annotations

import copy
import typing

import apm

from configflow import exceptions


FunctionType = typing.Callable[[typing.Any], typing.Any]
DictType = typing.Dict[str, typing.Any]


def deep_map(function: FunctionType, dictionary: DictType) -> DictType:
    """Apply a function to the values of a dictionary.

    Note
    ----
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

    return (
        apm.case(dictionary)
        .of(
            apm.InstanceOf(dict),
            lambda _: {key: deep_map(function, value) for key, value in dictionary.items()},
        )
        .of(apm.InstanceOf(list, set, tuple), lambda _: original_type(map(function, dictionary)))
        .otherwise(lambda _: function(dictionary))
    )


def update(to_dictionary: DictType, from_dictionary: DictType) -> DictType:
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
    {'db': {'host': 'localhost', 'ports': {'v1': 8000, 'v2': 5000, 'v3': 80}}, ...}
    """

    updated_dictionary = copy.deepcopy(to_dictionary)

    for key, value in from_dictionary.items():
        updated_dictionary[key] = (
            update(to_dictionary.get(key, {}), value)
            if isinstance(value, dict)
            else from_dictionary[key]
        )

    return updated_dictionary


def make_flat(
    dictionary: DictType,
    separator: str,
    parent_key: typing.Optional[str] = None,
) -> DictType:
    """Make a nested dictionary flat.

    Note
    ----
    If a value is a sequence ``list | tuple | set`` then ``make_flat``
    will use numerical indices as key identifiers.

    Examples
    --------
    >>> nested_dict = {
    ... "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
    ... "hub": {"env": "prod", "auth": "basic", "ports": [80, 50]},
    ... "timeout": 10,
    ... }
    >>> make_flat(nested_dict, separator="_")
    {'db_host': 'localhost', 'db_ports_v1': 8080, 'db_ports_v2': 5000, 'hub_env': 'prod', ...}
    """

    flatten_pairs = []  # type: ignore

    for key, value in dictionary.items():
        new_key = "".join((parent_key, separator, key)) if parent_key else key

        if isinstance(value, dict):
            pairs = make_flat(value, separator, new_key).items()
            flatten_pairs.extend(pairs)  # type: ignore

        else:
            flatten_pairs.append((new_key, value))

    return dict(flatten_pairs)


def make_nested(dictionary: DictType, separator: str) -> DictType:  # noqa: WPS231
    """Make a flat dictionary nested.

    Raises
    ------
    EmptyKeyError
        If a dictionary contains an empty key.

    DuplicatedKeyError
        If a dictionary contains a duplicated key.

    Examples
    --------
    >>> flat_dict = {
    ... "db_host": "localhost",
    ... "db_ports_v1": 8080,
    ... "db_ports_v2": 5000,
    ... "hub_env": "prod",
    ... "hub_auth": "basic",
    ... "hub_ports_0": 80,
    ... "hub_ports_1": 50,
    ... "timeout": 10,
    ... }
    >>> make_nested(flat_dict, separator="_")
    {'db': {'host': 'localhost', 'ports': {'v1': 8080, 'v2': 5000}}, ...}
    """

    nested_dictionary: DictType = {}

    for key, value in dictionary.items():
        if separator in key:
            inner_keys = key.split(separator)
            inner_dictionary = nested_dictionary

            for index, inner_key in enumerate(key.split(separator)):
                if inner_key == "":
                    raise exceptions.misc.EmptyKeyError(dictionary)

                elif index == len(inner_keys) - 1 and inner_key in inner_dictionary.keys():
                    raise exceptions.misc.DuplicatedKeyError(inner_key, dictionary)

                elif index == len(inner_keys) - 1:
                    inner_dictionary[inner_key] = value

                else:
                    if inner_key not in inner_dictionary.keys():
                        inner_dictionary[inner_key] = {}  # noqa: WPS220

                    elif not isinstance(inner_dictionary[inner_key], dict):
                        raise exceptions.misc.DuplicatedKeyError(  # noqa: WPS220
                            inner_key,
                            dictionary,
                        )

                    inner_dictionary = inner_dictionary[inner_key]
        else:
            nested_dictionary[key] = value

    return nested_dictionary
