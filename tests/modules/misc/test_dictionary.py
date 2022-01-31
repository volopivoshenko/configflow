"""Tests for the dictionary helper functions."""

from __future__ import annotations

import functools

from typing import Any
from typing import Callable
from typing import Dict

import pytest
import deepdiff

from configflow import misc


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
            marks=pytest.mark.xfail,
        ),
    ],
)
def test_deep_map(
    func: Callable[[Any], Any],
    input_dict: Dict[str, Any],
    expected_dict: Dict[str, Any],
) -> None:
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
def test_update(
    to_dict: Dict[str, Any],
    from_dict: Dict[str, Any],
    expected_dict: Dict[str, Any],
) -> None:
    """Test ``update`` function."""

    out_dict = misc.dictionary.update(to_dict, from_dict)
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
