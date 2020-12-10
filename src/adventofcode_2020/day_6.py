from functools import reduce
from typing import List
from typing import Set


def count_set_size(str_list: List[str]) -> int:
    used_words: Set[str] = set()
    used_words.update(*str_list)
    return len(used_words)


def count_all_sets(groups: List[List[str]]) -> List[int]:
    return [count_set_size(x) for x in groups]


def intersect_group_size(str_list: List[str]) -> int:
    group_sets = [
        set(
            x,
        )
        for x in str_list
    ]
    return len(reduce(lambda x, y: x.intersection(y), group_sets))


def intersect_all_sets(groups: List[List[str]]) -> List[int]:
    return [intersect_group_size(x) for x in groups]


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_6.txt", "r") as input_data:
        input = [x.splitlines() for x in input_data.read().split("\n\n")]
        print(f"Part 1: {sum(count_all_sets(input))}")
        print(f"Part 2: {sum(intersect_all_sets(input))}")
