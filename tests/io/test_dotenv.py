"""Tests for the implementation of the DOTENV IO functions."""

from pathlib import Path
from typing import Any
from typing import Dict

from configflow.io import dotenv


def test_loads(dotenv_stream: str, dotenv_dictionary: Dict[Any, Any]) -> None:
    """Test ``loads`` function."""

    assert dotenv_dictionary == dotenv.loads(dotenv_stream)


def test_loads_edge_cases() -> None:
    """Test ``loads`` function with edge cases."""

    empty_dict: Dict[Any, Any] = {}

    assert dotenv.loads("") == empty_dict
    assert dotenv.loads("value: 1") == empty_dict
    assert dotenv.loads("value=(1, 2, 3)") == {"value": (1, 2, 3)}


def test_load(dotenv_file: Path, dotenv_dictionary: Dict[Any, Any]) -> None:
    """Test ``load`` function."""

    with open(dotenv_file, "r") as env_file:
        dotenv_values = dotenv.load(env_file)

    assert dotenv_values == dotenv_dictionary
