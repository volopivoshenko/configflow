"""Tests for the implementation of the INI IO functions."""

from pathlib import Path
from typing import Any
from typing import Dict

from configflow.io import ini


def test_loads(ini_stream: str, ini_dictionary: Dict[Any, Any]) -> None:
    """Test ``loads`` function."""

    assert ini_dictionary == ini.loads(ini_stream)


def test_loads_edge_cases() -> None:
    """Test ``loads`` function with edge cases."""

    empty_dict: Dict[Any, Any] = {}

    assert ini.loads("") == empty_dict
    assert ini.loads("[default]\nvalue: 1") == {"default": {"value": 1}}
    assert ini.loads("[default]\nvalue=(1, 2, 3)") == {"default": {"value": (1, 2, 3)}}


def test_load(ini_file: Path, ini_dictionary: Dict[Any, Any]) -> None:
    """Test ``load`` function."""

    with open(ini_file, "r") as env_file:
        ini_values = ini.load(env_file)

    assert ini_values == ini_dictionary
