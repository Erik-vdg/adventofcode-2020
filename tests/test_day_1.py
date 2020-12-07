"""Test Cases for Day 1."""
import pytest

from adventofcode_2020.day_1 import part_1
from adventofcode_2020.day_1 import part_2


def test_part_1():
    test_list = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    results = part_1(test_list)
    assert results == 514579


def test_part_1_not_found():
    test_list = [
        1,
        2,
        3,
        4,
    ]
    with pytest.raises(ValueError):
        _ = part_1(test_list)


def test_part_2():
    test_list = [
        1721,
        979,
        366,
        299,
        675,
        1456,
    ]
    results = part_2(test_list)
    assert results == 241861950


def test_part_2_not_found():
    test_list = [
        1,
        2,
        3,
        4,
    ]
    with pytest.raises(ValueError):
        _ = part_2(test_list)
