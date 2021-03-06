"""Tests for the dictionary helper functions."""

from __future__ import annotations

import typing
import functools

import pytest
import deepdiff

from configflow import exceptions
from configflow import misc


FunctionType = typing.Callable[[typing.Any], typing.Any]
DictType = typing.Dict[str, typing.Any]


@pytest.mark.parametrize(
    "func,input_dict,expected_dict",
    [
        (
            int,
            {"db": {"db2": "50000", "mongo": {"v1": ["8000", "5000"]}}, "hub": "8080"},
            {"db": {"db2": 50000, "mongo": {"v1": [8000, 5000]}}, "hub": 8080},
        ),
        (
            functools.partial(lambda inc, port: port + inc, 1),
            {"db": {"db2": 50000, "mongo": {"v1": [8000, 5000]}}, "hub": 8080},
            {"db": {"db2": 50001, "mongo": {"v1": [8001, 5001]}}, "hub": 8081},
        ),
        (
            lambda port: int(port) if isinstance(port, str) else list(map(int, port)),
            {"db": {"db2": "50000", "mongo": {"v1": ["8000", ["80", "50"]]}}, "hub": "8080"},
            {"db": {"db2": 50000, "mongo": {"v1": [8000, [80, 50]]}}, "hub": 8080},
        ),
        pytest.param(
            int,
            {"db": {"db2": "50000", "mongo": {"v1": ["8000", ["80", "50"]]}}, "hub": "8080"},
            {"db": {"db2": 50000, "mongo": {"v1": [8000, ["80", "50"]]}}, "hub": 8080},
            marks=pytest.mark.xfail(raises=TypeError),
        ),
    ],
)
def test_deep_map(func: FunctionType, input_dict: DictType, expected_dict: DictType) -> None:
    """Test ``deep_map`` function."""

    out_dict = misc.dictionary.deep_map(func, input_dict)
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False


@pytest.mark.parametrize(
    "to_dict,from_dict,expected_dict",
    [
        (
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic"},
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8000, "v2": 5000, "v3": 80}},
                "hub": {"env": "dev"},
                "warnings": "suppress",
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8000, "v2": 5000, "v3": 80}},
                "hub": {"env": "dev", "auth": "basic"},
                "timeout": 10,
                "warnings": "suppress",
            },
        ),
        (
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic"},
                "timeout": 10,
            },
            {
                "hub": {"env": "dev"},
                "warnings": "suppress",
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "dev", "auth": "basic"},
                "timeout": 10,
                "warnings": "suppress",
            },
        ),
    ],
)
def test_update(to_dict: DictType, from_dict: DictType, expected_dict: DictType) -> None:
    """Test ``update`` function."""

    out_dict = misc.dictionary.update(to_dict, from_dict)
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False


@pytest.mark.parametrize(
    "separator,input_dict,expected_dict",
    [
        (
            "_",
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": [80, 50]},
                "timeout": 10,
            },
            {
                "db_host": "localhost",
                "db_ports_v1": 8080,
                "db_ports_v2": 5000,
                "hub_env": "prod",
                "hub_auth": "basic",
                "hub_ports": [80, 50],
                "timeout": 10,
            },
        ),
        (
            ".",
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": [80, 50]},
                "timeout": 10,
            },
            {
                "db.host": "localhost",
                "db.ports.v1": 8080,
                "db.ports.v2": 5000,
                "hub.env": "prod",
                "hub.auth": "basic",
                "hub.ports": [80, 50],
                "timeout": 10,
            },
        ),
    ],
)
def test_make_flat(separator: str, input_dict: DictType, expected_dict: DictType) -> None:
    """Test ``make_flat`` function."""

    out_dict = misc.dictionary.make_flat(input_dict, separator)
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False

    exp_out_dict = misc.dictionary.make_flat(expected_dict, separator)
    assert bool(deepdiff.DeepDiff(exp_out_dict, expected_dict)) is False


@pytest.mark.parametrize(
    "separator,input_dict,expected_dict",
    [
        (
            "_",
            {
                "db_host": "localhost",
                "db_ports_v1": 8080,
                "db_ports_v2": 5000,
                "hub_env": "prod",
                "hub_auth": "basic",
                "hub_ports_0": 80,
                "hub_ports_1": 50,
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": {"0": 80, "1": 50}},
                "timeout": 10,
            },
        ),
        (
            ".",
            {
                "db.host": "localhost",
                "db.ports.v1": 8080,
                "db.ports.v2": 5000,
                "hub.env": "prod",
                "hub.auth": "basic",
                "hub.ports.0": 80,
                "hub.ports.1": 50,
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": {"0": 80, "1": 50}},
                "timeout": 10,
            },
        ),
        pytest.param(
            "_",
            {
                "db__host": "localhost",
                "db_ports_v1": 8080,
                "db_ports_v2": 5000,
                "hub_env": "prod",
                "hub_auth": "basic",
                "hub_ports_0": 80,
                "hub_ports_1": 50,
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": {"0": 80, "1": 50}},
                "timeout": 10,
            },
            marks=pytest.mark.xfail(raises=exceptions.misc.EmptyKeyError),
        ),
        pytest.param(
            "_",
            {
                "db_host": "localhost",
                "db_ports_v1": 8080,
                "db_ports_v2": 5000,
                "hub_env": "prod",
                "hub_auth": "basic",
                "hub_ports_0": 80,
                "hub_ports_1": 50,
                "hub_ports": 5050,
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": {"0": 80, "1": 50}},
                "timeout": 10,
            },
            marks=pytest.mark.xfail(raises=exceptions.misc.DuplicatedKeyError),
        ),
        pytest.param(
            "_",
            {
                "db_host": "localhost",
                "db_ports_v1": 8080,
                "db_ports_v2": 5000,
                "hub_env": "prod",
                "hub_auth": "basic",
                "hub_ports": 5050,
                "hub_ports_0": 80,
                "hub_ports_1": 50,
                "timeout": 10,
            },
            {
                "db": {"host": "localhost", "ports": {"v1": 8080, "v2": 5000}},
                "hub": {"env": "prod", "auth": "basic", "ports": {"0": 80, "1": 50}},
                "timeout": 10,
            },
            marks=pytest.mark.xfail(raises=exceptions.misc.DuplicatedKeyError),
        ),
    ],
)
def test_make_nested(separator: str, input_dict: DictType, expected_dict: DictType) -> None:
    """Test ``make_nested`` function."""

    out_dict = misc.dictionary.make_nested(input_dict, separator)
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False

    exp_out_dict = misc.dictionary.make_nested(expected_dict, separator)
    assert bool(deepdiff.DeepDiff(exp_out_dict, expected_dict)) is False
