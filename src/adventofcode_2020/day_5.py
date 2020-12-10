from dataclasses import dataclass


@dataclass
class Seat:
    row: int
    column: int

    @classmethod
    def from_boarding_pass(cls, boarding_pass: str) -> "Seat":
        min_row = 0
        max_row = 127

        for char in boarding_pass[:-3]:
            if char == "F":
                max_row = int(max_row - (max_row - min_row + 1) / 2)
            elif char == "B":
                min_row = int(min_row + (max_row - min_row + 1) / 2)

        min_col = 0
        max_col = 7

        for char in boarding_pass[-3:]:
            if char == "L":
                max_col = int(max_col - (max_col - min_col + 1) / 2)
            elif char == "R":
                min_col = int(min_col + (max_col - min_col + 1) / 2)
        return cls(row=max_row, column=max_col)

    @property
    def id(self) -> int:
        return self.row * 8 + self.column


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_5.txt", "r") as input_data:
        boarding_passes = input_data.read().splitlines()
        seats = [Seat.from_boarding_pass(p) for p in boarding_passes]
        ids = sorted([seat.id for seat in seats])
        highest_id = max(ids)
        print(f"Part 1: {highest_id}")

        for i in range(1, 128 * 8 - 1):
            if i not in ids:
                if i + 1 in ids and i - 1 in ids:
                    print(f"Part 2: {i}")
                    break
