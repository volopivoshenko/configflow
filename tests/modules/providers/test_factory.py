"""Tests for the factory that returns an IO provider based on a file type."""

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
from configflow import providers


DictType = typing.Dict[str, typing.Any]


@pytest.mark.parametrize(
    "filepath,expected_provider,expected_dict",
    [
        (
            "tests/fixtures/example.ini",
            providers.ini,
            pytest.lazy_fixture("expected_ini_dict"),
        ),
        (
            "tests/fixtures/example.env",
            providers.dotenv,
            pytest.lazy_fixture("expected_dotenv_dict"),
        ),
        (
            "tests/fixtures/example.yaml",
            providers.yaml,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        (
            "tests/fixtures/example.json",
            json,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        (
            "tests/fixtures/example.toml",
            providers.toml,
            pytest.lazy_fixture("expected_yaml_dict"),
        ),
        (
            "tests/fixtures/example.properties",
            providers.properties,
            pytest.lazy_fixture("expected_properties_dict"),
        ),
        pytest.param(
            "tests/fixtures/example.yacl",
            providers.toml,
            pytest.lazy_fixture("expected_yaml_dict"),
            marks=pytest.mark.xfail(raises=exceptions.providers.FileTypeError),
        ),
    ],
)
def test_get_loader(
    filepath: str,
    expected_provider: types.ModuleType,
    expected_dict: DictType,
) -> None:
    """Test ``get_provider`` function."""

    provider = providers.factory.get_provider(pathlib.Path(filepath))

    with open(filepath, "r") as fixture_file:
        out_dict = provider.load(fixture_file)

    assert provider == expected_provider
    assert bool(deepdiff.DeepDiff(out_dict, expected_dict)) is False
