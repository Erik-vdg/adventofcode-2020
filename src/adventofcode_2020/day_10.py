from functools import lru_cache
from typing import Dict
from typing import List
from typing import Tuple


def jolt_differences(jolt_list: List[int]) -> Dict[int, int]:
    sorted_list = sorted(jolt_list)
    sorted_list.insert(0, 0)
    ret_dict = {1: 0, 2: 0, 3: 0}
    for i, item in enumerate(sorted_list[:-1]):
        ret_dict[sorted_list[i + 1] - item] += 1
    ret_dict[3] += 1
    return ret_dict


def jolt_arrangements(jolt_list: List[int]) -> int:
    @lru_cache(maxsize=None)
    def explode_for_reasons(onehot_list: Tuple[bool, ...]) -> int:
        if onehot_list == (True,):
            return 1
        elif len(onehot_list) == 0:
            return 0
        elif len(onehot_list) > 1 and onehot_list[-1]:
            result = (
                explode_for_reasons(onehot_list[:-1])
                + explode_for_reasons(onehot_list[:-2])
                + explode_for_reasons(onehot_list[:-3])
            )
            return result
        else:
            return 0

    mylist = jolt_list.copy()
    mylist.extend([0, max(jolt_list) + 3])
    encoded_list = [False] * (max(mylist) + 1)
    for item in mylist:
        encoded_list[item] = True
    thing = tuple(encoded_list)
    return explode_for_reasons(thing)


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_10.txt", "r") as input_data:
        input = [int(x) for x in input_data.read().splitlines()]
        part_1 = jolt_differences(input)
        print(f"Part 1 Answer: {part_1[1] * part_1[3]}")
        part_2 = jolt_arrangements(input)
        print(f"Part 2 Answer: {part_2}")
