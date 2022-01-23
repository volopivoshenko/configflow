"""Tests for the string helper functions and primitive data types."""

from __future__ import annotations

from typing import Union

import pytest

from configflow import misc


@pytest.mark.parametrize(
    "input_value,expected_value",
    [
        ("yamper", "yamper"),
        ("1418", 1418),
        ("0.485", 0.485),
        ("[:]", None),
        ("[10, 'sneasel']", [10, "sneasel"]),
        ("(10, 'naganadel')", (10, "naganadel")),
        ("{10, 'snivy'}", {10, "snivy"}),
        ("{'pokemon': 'pidove', 'rank': '1'}", {"pokemon": "pidove", "rank": "1"}),
        (
            "['85', '0.23', 'cleffa', ['10', ['0.123'], 'blipbug']]",
            [85, 0.23, "cleffa", [10, [0.123], "blipbug"]],
        ),
    ],
)
def test_parse(
    input_value: str,
    expected_value: Union[str, int, float],
) -> None:
    """Test ``parse`` function."""

    assert misc.string.parse(input_value) == expected_value
    assert misc.string.parse(expected_value) == expected_value  # type: ignore