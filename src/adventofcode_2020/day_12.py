from enum import Enum
from typing import Callable
from typing import Dict
from typing import List
from typing import Tuple

from adventofcode_2020.utils import Coordinate


class Bearing(Enum):
    NORTH: int = 0
    WEST: int = 1
    SOUTH: int = 2
    EAST: int = 3


class Action(Enum):
    NORTH: str = "N"
    SOUTH: str = "S"
    EAST: str = "E"
    WEST: str = "W"
    FORWARD: str = "F"
    ROTATELEFT: str = "L"
    ROTATERIGHT: str = "R"


instruction_map_p1: Dict[
    Action, Callable[[Bearing, Coordinate, int], Tuple[Bearing, Coordinate]]
] = {
    Action.NORTH: lambda bearing, coords, value: (
        bearing,
        coords + Coordinate(0, value),
    ),
    Action.SOUTH: lambda bearing, coords, value: (
        bearing,
        coords + Coordinate(0, -value),
    ),
    Action.EAST: lambda bearing, coords, value: (
        bearing,
        coords + Coordinate(value, 0),
    ),
    Action.WEST: lambda bearing, coords, value: (
        bearing,
        coords + Coordinate(-value, 0),
    ),
    Action.FORWARD: lambda bearing, coords, value: instruction_map_p1[
        Action[bearing.name]
    ](bearing, coords, value),
    Action.ROTATELEFT: lambda bearing, coords, value: (
        Bearing((bearing.value + (value / 90)) % 4),
        coords,
    ),
    Action.ROTATERIGHT: lambda bearing, coords, value: (
        Bearing((bearing.value - (value / 90)) % 4),
        coords,
    ),
}


def process_nav_instructions_p1(
    starting_bearing: Bearing,
    starting_coords: Coordinate,
    instruction_list: List[str],
) -> Tuple[Bearing, Coordinate]:

    bearing = starting_bearing
    coords = starting_coords

    for instruction in instruction_list:
        action = Action(instruction[0])
        value = int(instruction[1:])

        bearing, coords = instruction_map_p1[action](bearing, coords, value)

    return bearing, coords


instruction_map_p2: Dict[
    Action, Callable[[Coordinate, Coordinate, int], Tuple[Coordinate, Coordinate]]
] = {
    Action.NORTH: lambda coords, waypoint, value: (
        coords,
        waypoint + Coordinate(0, value),
    ),
    Action.SOUTH: lambda coords, waypoint, value: (
        coords,
        waypoint + Coordinate(0, -value),
    ),
    Action.EAST: lambda coords, waypoint, value: (
        coords,
        waypoint + Coordinate(value, 0),
    ),
    Action.WEST: lambda coords, waypoint, value: (
        coords,
        waypoint + Coordinate(-value, 0),
    ),
    Action.FORWARD: lambda coords, waypoint, value: (
        coords + waypoint * value,
        waypoint,
    ),
    Action.ROTATELEFT: lambda coords, waypoint, value: (coords, waypoint.rotate(value)),
    Action.ROTATERIGHT: lambda coords, waypoint, value: (
        coords,
        waypoint.rotate(-value),
    ),
}


def process_nav_instructions_p2(
    starting_coords: Coordinate,
    starting_waypoint: Coordinate,
    instruction_list: List[str],
) -> Tuple[Coordinate, Coordinate]:

    coords = starting_coords
    waypoint = starting_waypoint

    for instruction in instruction_list:
        action = Action(instruction[0])
        value = int(instruction[1:])

        coords, waypoint = instruction_map_p2[action](coords, waypoint, value)

    return coords, waypoint


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_12.txt", "r") as input_data:
        input = input_data.read().splitlines()

        starting_bearing = Bearing.EAST
        starting_coords = Coordinate(0, 0)

        final_bearing, final_coords = process_nav_instructions_p1(
            starting_bearing, starting_coords, input
        )
        print(f"Part 1 Answer: {abs(final_coords.x) + abs(final_coords.y)}")

        starting_waypoint = Coordinate(10, 1)
        final_coords, final_waypoint = process_nav_instructions_p2(
            starting_coords, starting_waypoint, input
        )
        print(f"Part 2 Answer: {abs(final_coords.x) + abs(final_coords.y)}")
