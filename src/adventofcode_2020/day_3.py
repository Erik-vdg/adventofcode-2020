import operator
from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Point:
    row: int
    column: int

    def __add__(self, other_point: "Point") -> "Point":
        return self.__class__(
            self.row + other_point.row, self.column + other_point.column
        )


@dataclass
class TreeMap:
    """The field is a list of lists, containing bools. a true value represents a tree."""

    field: List[List[bool]]

    @classmethod
    def from_str_list(cls, str_list: List[str]) -> "TreeMap":
        field = []
        for line in str_list:
            field.append([x == "#" for x in line])
        return cls(field)

    @property
    def height(self) -> int:
        return len(self.field)

    @property
    def width(self) -> int:
        return len(self.field[0])

    def collides(self, point: Point) -> bool:
        return self.field[point.row][point.column]

    def reached_bottom(self, point: Point) -> bool:
        return self.height <= point.row

    def travel_step(self, starting_location: Point, travel_slope: Point) -> Point:
        new_point = starting_location + travel_slope
        new_point.column %= self.width
        return new_point


def part_1(str_list: List[str], travel_vector: Point) -> int:
    tree_map = TreeMap.from_str_list(str_list)
    tobboggan_position = Point(0, 0)
    collision_counter = 0
    while tree_map.reached_bottom(tobboggan_position) is False:
        if tree_map.collides(tobboggan_position):
            collision_counter += 1
        tobboggan_position = tree_map.travel_step(tobboggan_position, travel_vector)
    return collision_counter


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_3.txt", "r") as input_data:
        raw_map_data = input_data.read().splitlines()
        collision_count_p1 = part_1(raw_map_data, Point(1, 3))
        print(f"Part 1: {collision_count_p1}")

        slopes_to_check = [
            Point(1, 1),
            Point(1, 3),
            Point(1, 5),
            Point(1, 7),
            Point(2, 1),
        ]
        collision_counts = [part_1(raw_map_data, slope) for slope in slopes_to_check]
        collision_count_p2 = reduce(operator.mul, collision_counts, 1)
        print(f"Part 2: {collision_count_p2}")
