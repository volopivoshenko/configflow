"""Tests for the factory that returns the IO module based on a file type."""

from __future__ import annotations

import json
import types
import typing
import pathlib

import toml
import yaml
import pytest
import deepdiff

from configflow import exceptions
from configflow import io


DictType = typing.Dict[str, typing.Any]


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
    expected_loader: types.ModuleType,
    expected_dict: DictType,
) -> None:
    """Test ``get_loader & load`` functions."""

    loader = io.loader.get_loader(pathlib.Path(filepath))

    with open(filepath, "r") as fixture_file:
        out_dict = loader(fixture_file)

    assert loader == expected_loader
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
