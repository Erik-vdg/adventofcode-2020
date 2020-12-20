from adventofcode_2020.day_10 import jolt_arrangements
from adventofcode_2020.day_10 import jolt_differences


def test_part_1():
    input = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]
    result = jolt_differences(input)
    assert result[1] == 7
    assert result[3] == 5


def test_part_2():
    input = [
        16,
        10,
        15,
        5,
        1,
        11,
        7,
        19,
        6,
        12,
        4,
    ]
    result = jolt_arrangements(input)
    assert result == 8

    input_2 = [
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
    result = jolt_arrangements(input_2)
    assert result == 19208
