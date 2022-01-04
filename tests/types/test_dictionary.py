"""Tests for the helper functions and data types for the dictionary."""

import pytest

from configflow.types import dictionary


def test_convert_type() -> None:
    """Test ``convert_type`` function."""

    assert dictionary.convert_type("string") == "string"

    assert dictionary.convert_type("1") == 1
    assert pytest.approx(dictionary.convert_type("0.1"), 0.1)

    assert dictionary.convert_type("('1', '2', 3)") == (1, 2, 3)
    assert dictionary.convert_type("['1', '2', 3]") == [1, 2, 3]
    assert dictionary.convert_type("{'1', '2', 3}") == {1, 2, 3}

    assert dictionary.convert_type("None") is None
    assert dictionary.convert_type(":") is None


def test_deep_map() -> None:
    """Test ``deep_map`` function."""


