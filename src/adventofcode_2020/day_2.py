"""Day 2 Implementation."""
from dataclasses import dataclass
from typing import List


@dataclass
class PasswordPolicy:
    """Class to keep track of a password rule."""

    lower_bound: int
    upper_bound: int
    character_rule: str
    password: str

    @classmethod
    def from_raw_specification(cls, raw_spec: str) -> "PasswordPolicy":
        """Creates a PasswordPolicy from a line of puzzle input."""
        components = raw_spec.split(" ")
        lower_bound, upper_bound = components[0].split("-")
        character_rule = components[1].rstrip(":")
        password = components[2]
        return cls(
            int(lower_bound),
            int(upper_bound),
            character_rule,
            password,
        )

    def is_valid_p1(self) -> bool:
        """Checks if this password matches its policy for part 1."""
        return (
            self.lower_bound
            <= self.password.count(self.character_rule)
            <= self.upper_bound
        )

    def is_valid_p2(self) -> bool:
        """Checks if this password matches its policy for part 2."""
        return (self.password[self.lower_bound - 1] == self.character_rule) ^ (
            self.password[self.upper_bound - 1] == self.character_rule
        )


def part_1(raw_password_specifications: List[str]) -> List[bool]:
    """Part 1 Solution."""
    return [
        PasswordPolicy.from_raw_specification(raw_policy).is_valid_p1()
        for raw_policy in raw_password_specifications
    ]


def part_2(raw_password_specifications: List[str]) -> List[bool]:
    """Part 1 Solution."""
    return [
        PasswordPolicy.from_raw_specification(raw_policy).is_valid_p2()
        for raw_policy in raw_password_specifications
    ]


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_2.txt", "r") as input_data:
        raw_password_specifications = input_data.readlines()
        validated_passwords = part_1(raw_password_specifications)
        valid_password_count = sum(validated_passwords)
        print(f"Part 1: {valid_password_count}")

        validated_passwords = part_2(raw_password_specifications)
        valid_password_count = sum(validated_passwords)
        print(f"Part 2: {valid_password_count}")
