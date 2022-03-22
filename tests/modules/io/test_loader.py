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
            pytest.lazy_fixture("expected_ini_dict"),
        ),
        (
            "tests/fixtures/example.env",
            io.dotenv.load,
            pytest.lazy_fixture("expected_dotenv_dict"),
        ),
        (
            "tests/fixtures/example.yaml",
            yaml.safe_load,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        (
            "tests/fixtures/example.json",
            json.load,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        (
            "tests/fixtures/example.toml",
            toml.load,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        pytest.param(
            "tests/fixtures/example.conf",
            toml.load,
            pytest.lazy_fixture("expected_yaml_dict"),
            marks=pytest.mark.xfail(raises=exceptions.io.FileTypeError),
        ),
    ],
)
def test_get_loader(
    filepath: str,
    expected_loader: ModuleType,
    expected_dict: Dict[str, Any],
) -> None:
    """Test ``get_loader & load`` functions."""

    loader = io.loader.get_loader(Path(filepath))

    with open(filepath, "r") as fixture_file:
        out_dict = loader(fixture_file)

    assert loader == expected_loader
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
