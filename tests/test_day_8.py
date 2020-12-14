import pytest

from adventofcode_2020.day_8 import fix_instructions
from adventofcode_2020.day_8 import run_instructions


@pytest.fixture
def instruction_list():
    return [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ]


def test_instructions_infinite(instruction_list):
    is_infinite, result = run_instructions(instruction_list)
    assert is_infinite is True
    assert result == 5


def test_instructions_fix(instruction_list):
    result = fix_instructions(instruction_list)
    assert result == 8
