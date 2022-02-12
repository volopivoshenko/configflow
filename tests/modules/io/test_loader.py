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
    "filepath,expected_loader,expected_dict",
    [
        (
            "tests/fixtures/example.ini",
            io.ini.load,
            pytest.lazy_fixture("expected_ini_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.env",
            io.dotenv.load,
            pytest.lazy_fixture("expected_dotenv_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.yaml",
            yaml.safe_load,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.json",
            json.load,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        (
            "tests/fixtures/example.toml",
            toml.load,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
        ),
        pytest.param(
            "tests/fixtures/example.config",
            toml.load,
            pytest.lazy_fixture("expected_yaml_dict"),  # type: ignore[attr-defined]
            marks=pytest.mark.xfail(raises=exceptions.io.InvalidFileTypeError),
        ),
    ],
)
def test_get_loader(
    filepath: str,
    expected_loader: ModuleType,
    expected_dict: Dict[str, Any],
) -> None:
    """Test ``get_loader | load`` functions."""

    loader = io.loader.get_loader(Path(filepath))

    with open(filepath, "r") as fixture_file:
        out_dict = loader(fixture_file)

    assert loader == expected_loader
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
