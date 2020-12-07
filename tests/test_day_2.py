"""Day 2 Tests."""
from adventofcode_2020.day_2 import part_1
from adventofcode_2020.day_2 import part_2


def test_part_1():
    input = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    expected_output = [True, False, True]
    found_output = part_1(input)
    assert expected_output == found_output


def test_part_2():
    input = [
        "1-3 a: abcde",
        "1-3 b: cdefg",
        "2-9 c: ccccccccc",
    ]
    expected_output = [True, False, False]
    found_output = part_2(input)
    assert expected_output == found_output
