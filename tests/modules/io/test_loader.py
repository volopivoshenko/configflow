"""Tests for the factory that returns the IO module based on a file type."""

from __future__ import annotations

import json

from pathlib import Path
from types import ModuleType
from typing import Any
from typing import Dict

import toml
import yaml
import pytest
import deepdiff

from configflow import exceptions
from configflow import io


@pytest.mark.parametrize(
    "filepath,expected_io_module,expected_dict",
    [
        (
            "tests/fixtures/example.ini",
            io.ini,
            pytest.lazy_fixture("expected_ini_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.env",
            io.dotenv,
            pytest.lazy_fixture("expected_dotenv_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.yaml",
            yaml,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.json",
            json,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.toml",
            toml,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        pytest.param(
            "tests/fixtures/example.config",
            toml,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
            marks=pytest.mark.xfail(raises=exceptions.io.InvalidFileTypeError),
        ),
    ],
)
def test_get_io_module_load(
    filepath: str,
    expected_io_module: ModuleType,
    expected_dict: Dict[str, Any],
) -> None:
    """Test ``get_io_module | load`` functions."""

    io_module = io.loader.get_io_module(Path(filepath))

    with open(filepath, "r") as fixture_file:
        # noinspection PyUnresolvedReferences
        out_dict = io_module.load(fixture_file)

    assert io_module.__name__ == expected_io_module.__name__
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
