from adventofcode_2020.day_3 import part_1
from adventofcode_2020.day_3 import Point


def test_part_1():
    input = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]

    expected_collisions = 7
    found_collisions = part_1(input, Point(1, 3))
    assert expected_collisions == found_collisions
