"""Day 1!"""
from typing import List


def part_1(input_list: List[int], required_sum: int = 2020) -> int:
    for i, x in enumerate(input_list, 0):
        for _, y in enumerate(input_list, i):
            if x + y == required_sum:
                return x * y
    raise ValueError("Required Sum not Found!")


def part_2(input_list: List[int], required_sum: int = 2020) -> int:
    for i, x in enumerate(input_list, 0):
        for j, y in enumerate(input_list, i):
            for _, z in enumerate(input_list, j):
                if x + y + z == required_sum:
                    return x * y * z
    raise ValueError("Required Sum not Found!")


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_1.txt", "r") as input_data:
        input_list = [int(i) for i in input_data.readlines()]
        part_1_result = part_1(input_list)
        print(f"Part 1 result: {part_1_result}")

        part_2_result = part_2(input_list)
        print(f"Part 2 result: {part_2_result}")
