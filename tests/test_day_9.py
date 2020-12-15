import pytest

from adventofcode_2020.day_9 import find_weakness
from adventofcode_2020.day_9 import process_list


@pytest.fixture
def test_data():
    return [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]


def test_process_list(test_data):
    result = process_list(num_list=test_data, preamble_length=5)
    assert result == 127


def test_find_weakness(test_data):
    result = find_weakness(test_data, 127)
    assert result == 62
