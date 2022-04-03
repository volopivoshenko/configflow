"""Tests for the file configuration source."""

from __future__ import annotations

import os

from pathlib import Path
from typing import Any
from typing import Dict

import pytest
import deepdiff
import pytest_mock

from configflow import exceptions
from configflow import sources


def test_filepath_path(expected_filepath: Path) -> None:
    """Test ``filepath`` property."""

    source = sources.FileSource(path=expected_filepath)
    assert source.filepath == expected_filepath


def test_filepath_environment_variable(
    expected_filepath: Path,
    mocker: pytest_mock.MockerFixture,
) -> None:
    """Test ``filepath`` property."""

    mocker.patch.dict(os.environ, {"DEV_CONFIG": expected_filepath.as_posix()})
    source = sources.FileSource(environment_variable="DEV_CONFIG")
    assert source.filepath == expected_filepath


def test_filepath_command_line_argument(
    expected_filepath: Path,
    mocker: pytest_mock.MockerFixture,
) -> None:
    """Test ``filepath`` property."""

    mocker.patch("sys.argv", ["-c", expected_filepath.as_posix()])
    source = sources.FileSource(command_line_argument="-c")
    assert source.filepath == expected_filepath

    with pytest.raises(exceptions.sources.CommandLineArgumentError):
        mocker.patch("sys.argv", ["-c"])
        source = sources.FileSource(command_line_argument="-c")
        _ = source.filepath

    with pytest.raises(exceptions.sources.CommandLineArgumentError):
        mocker.patch("sys.argv", [])
        source = sources.FileSource(command_line_argument="-c")
        _ = source.filepath


def test_filepath_empty() -> None:
    """Test ``filepath`` property."""

    with pytest.raises(exceptions.sources.SourceError):
        source = sources.FileSource()
        _ = source.filepath


def test_content(expected_filepath: Path, expected_content: Dict[str, Any]) -> None:
    """Test ``content`` property."""

    source = sources.FileSource(path=expected_filepath)
    assert bool(deepdiff.DeepDiff(source.content, expected_content)) is False
