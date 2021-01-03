from adventofcode_2020.day_12 import (
    Bearing,
    process_nav_instructions_p1,
    process_nav_instructions_p2,
)
from adventofcode_2020.utils import Coordinate


def test_process_instructions_p1():
    instructions = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]
    bearing = Bearing.EAST
    coords = Coordinate(0, 0)
    expected_bearing = Bearing.SOUTH
    expected_coords = Coordinate(17, -8)

    bearing, coords = process_nav_instructions_p1(bearing, coords, instructions)

    assert bearing == expected_bearing
    assert coords == expected_coords


def test_process_instructions_p2():
    instructions = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11",
    ]
    coords = Coordinate(0, 0)
    waypoint = Coordinate(10, 1)

    expected_coords = Coordinate(214, -72)
    expected_waypoint = Coordinate(4, -10)

    coords, waypoint = process_nav_instructions_p2(coords, waypoint, instructions)

    assert coords == expected_coords
    assert waypoint == expected_waypoint
