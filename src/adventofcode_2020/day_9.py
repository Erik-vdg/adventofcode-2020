from typing import List

from adventofcode_2020.day_1 import part_1


def process_list(num_list: List[int], preamble_length: int) -> int:
    prior = num_list[:preamble_length]
    for num in num_list[preamble_length:]:
        try:
            _ = part_1(prior, num)
            prior = prior[1:]
            prior.append(num)
        except ValueError:
            return num
    return -1


def find_weakness(num_list: List[int], invalid_num: int) -> int:
    small_index = 0
    big_index = 1
    while True:
        num_range = num_list[small_index:big_index]
        test_result = sum(num_range)
        if test_result < invalid_num:
            big_index += 1
        elif test_result > invalid_num:
            small_index += 1
            big_index = small_index + 1
        else:
            return min(num_range) + max(num_range)


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_9.txt", "r") as input_data:
        input = [int(x) for x in input_data.read().splitlines()]
        result_1 = process_list(input, 25)
        print(f"Part 1 Answer: {result_1}")

        result_2 = find_weakness(input, result_1)
        print(f"Part 2 Answer: {result_2}")
