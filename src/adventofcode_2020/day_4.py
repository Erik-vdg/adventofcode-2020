import re
from typing import Dict
from typing import List
from typing import Optional
from typing import Type
from typing import TypeVar

import attr


@attr.s
class Passport:
    birth_year: str = attr.ib()
    issue_year: str = attr.ib()
    expiration_year: str = attr.ib()
    height: str = attr.ib()
    hair_color: str = attr.ib()
    eye_color: str = attr.ib()
    passport_id: str = attr.ib()
    country_id: Optional[str] = attr.ib()

    @classmethod
    def from_dict(cls, input: Dict[str, str]) -> "Passport":
        return cls(
            birth_year=input["byr"],
            issue_year=input["iyr"],
            expiration_year=input["eyr"],
            height=input["hgt"],
            hair_color=input["hcl"],
            eye_color=input["ecl"],
            passport_id=input["pid"],
            country_id=input.get("cid", None),
        )


@attr.s
class ValidatedPassport:
    birth_year: str = attr.ib()
    issue_year: str = attr.ib()
    expiration_year: str = attr.ib()
    height: str = attr.ib()
    hair_color: str = attr.ib()
    eye_color: str = attr.ib()
    passport_id: str = attr.ib()
    country_id: Optional[str] = attr.ib()

    @classmethod
    def from_dict(cls, input: Dict[str, str]) -> "ValidatedPassport":
        return cls(
            birth_year=input["byr"],
            issue_year=input["iyr"],
            expiration_year=input["eyr"],
            height=input["hgt"],
            hair_color=input["hcl"],
            eye_color=input["ecl"],
            passport_id=input["pid"],
            country_id=input.get("cid", None),
        )

    @birth_year.validator
    def validate_birth_year(self, _: str, value: str) -> None:
        if not 1920 <= int(value) <= 2002:
            print(f"birth_year: {value}")
            raise ValueError

    @issue_year.validator
    def validate_issue_year(self, _: str, value: str) -> None:
        if not 2010 <= int(value) <= 2020:
            print(f"issue_year: {value}")
            raise ValueError

    @expiration_year.validator
    def validate_expiration_year(self, _: str, value: str) -> None:
        if not 2020 <= int(value) <= 2030:
            print(f"exp_year: {value}")
            raise ValueError

    @height.validator
    def validate_height(self, _: str, value: str) -> None:
        height = value[:-2]
        units = value[-2:]
        if (150 <= int(height) <= 193 and units == "cm") or (
            59 <= int(height) <= 76 and units == "in"
        ):
            pass
        else:
            print(f"height: {value}")
            raise ValueError

    @hair_color.validator
    def validate_hair_color(self, _: str, value: str) -> None:
        if not re.match(r"^#[0-9a-f]{6}$", value):
            print(f"hair_color: {value}")
            raise ValueError

    @eye_color.validator
    def validate_eye_color(self, _: str, value: str) -> None:
        if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print(f"eye_color: {value}")
            raise ValueError

    @passport_id.validator
    def validate_passport_id(self, _: str, value: str) -> None:
        if not re.match(r"^[0-9]{9}$", value):
            print(f"passport_id: {value}")
            raise ValueError


P = TypeVar("P", Passport, ValidatedPassport)


def input_to_passports(input: List[str], passport_type: Type[P]) -> List[P]:
    passports = []
    buf = []
    for line in input:
        if line != "":
            buf.append(line)
        else:
            raw_passport = " ".join(buf).split(" ")
            passport_creation_dict = {
                pair.split(":")[0]: pair.split(":")[1] for pair in raw_passport
            }
            try:
                passports.append(passport_type.from_dict(passport_creation_dict))
                print(passport_creation_dict)
            except ValueError:
                pass
            except KeyError:
                pass
            buf = []
    return passports


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_4.txt", "r") as input_data:
        input = input_data.read().splitlines()
        passports = input_to_passports(input, Passport)

        print(f"Part 1 answer: {len(passports)}")

        validated_passports = input_to_passports(input, ValidatedPassport)
        print(f"Part 2 answer: {len(validated_passports) + 1}")
