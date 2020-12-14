from typing import List
from typing import Set
from typing import Tuple


def parse_instruction(instruction: str) -> Tuple[int, int]:
    operation, argument = instruction.split(" ")
    if operation == "acc":
        return 1, int(argument)
    elif operation == "jmp":
        return int(argument), 0
    elif operation == "nop":
        return 1, 0
    else:
        raise NotImplementedError


def run_instructions(instruction_list: List[str]) -> Tuple[bool, int]:
    acc = 0
    line_num = 0
    visited_lines: Set[int] = set()
    while True:
        try:
            instruction = instruction_list[line_num]
        except IndexError:
            # Program completed successfully!
            return False, acc
        line_inc, acc_inc = parse_instruction(instruction)
        line_num += line_inc
        if line_num in visited_lines:
            # Infinite Loop
            return True, acc
        else:
            visited_lines.add(line_num)
            acc += acc_inc


def fix_instructions(instruction_list: List[str]) -> int:
    for i, instruction in enumerate(instruction_list):
        operation, argument = instruction.split(" ")
        temp_instruction_list = instruction_list.copy()
        if operation == "acc":
            pass
        elif operation == "jmp":
            temp_instruction_list[i] = f"nop {argument}"
        elif operation == "nop":
            temp_instruction_list[i] = f"jmp {argument}"
        is_infinite, acc = run_instructions(temp_instruction_list)
        if is_infinite is False:
            return acc
    return -1


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_8.txt", "r") as input_data:
        input = input_data.read().splitlines()
        _, result = run_instructions(input)

        print(f"Part 1: {result}")

        result_2 = fix_instructions(input)

        print(f"Part 2: {result_2}")
