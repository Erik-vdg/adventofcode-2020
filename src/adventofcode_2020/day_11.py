from typing import Dict, List, Iterator, Mapping
import attr
from enum import Enum


@attr.s(frozen=True)
class Coordinate:
    x: int = attr.ib()
    y: int = attr.ib()

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return self.__class__(x=self.x + other.x, y=self.y + other.y)

    def __mul__(self, other: int) -> "Coordinate":
        return self.__class__(x=self.x * other, y=self.y * other)

    def __rmul__(self, other: int) -> "Coordinate":
        return self.__class__(x=self.x * other, y=self.y * other)


class SeatStatus(Enum):
    VACANT: str = "L"
    OCCUPIED: str = "#"
    FLOOR: str = "."


class SeatMap(Mapping[Coordinate, SeatStatus]):
    __seat_dict: Dict[Coordinate, SeatStatus]

    def __init__(self, input: Dict[Coordinate, SeatStatus]):
        self.__seat_dict = input

    @classmethod
    def from_input(cls, input: List[str]) -> "SeatMap":
        seat_dict = {}
        for row, line in enumerate(input):
            for col, thing in enumerate(line):
                seat_dict[Coordinate(row, col)] = SeatStatus(thing)
        return cls(seat_dict)

    # def __contains__(self, item: Coordinate) -> bool:
    #     return item in self.__seat_dict

    def __getitem__(self, item: Coordinate) -> SeatStatus:
        return self.__seat_dict.get(item, SeatStatus.VACANT)

    def __len__(self) -> int:
        return len(self.__seat_dict)

    def __iter__(self) -> Iterator[Coordinate]:
        return iter(self.__seat_dict)

    def adjacent_neighbors(self, item: Coordinate) -> Dict[SeatStatus, int]:
        ret = {
            SeatStatus.FLOOR: 0,
            SeatStatus.OCCUPIED: 0,
            SeatStatus.VACANT: 0,
        }
        neighbor_mask = [
            Coordinate(-1, -1),
            Coordinate(-1, 0),
            Coordinate(-1, 1),
            Coordinate(0, -1),
            Coordinate(0, 1),
            Coordinate(1, -1),
            Coordinate(1, 0),
            Coordinate(1, 1),
        ]
        for coord in neighbor_mask:
            ret[self[item + coord]] += 1
        return ret

    def visible_neighbors(self, item: Coordinate) -> Dict[SeatStatus, int]:
        ret = {
            SeatStatus.FLOOR: 0,
            SeatStatus.OCCUPIED: 0,
            SeatStatus.VACANT: 0,
        }
        neighbor_mask = [
            Coordinate(-1, -1),
            Coordinate(-1, 0),
            Coordinate(-1, 1),
            Coordinate(0, -1),
            Coordinate(0, 1),
            Coordinate(1, -1),
            Coordinate(1, 0),
            Coordinate(1, 1),
        ]
        for coord in neighbor_mask:
            temp_coord = coord
            while self[item + temp_coord] is SeatStatus.FLOOR:
                temp_coord += coord
            ret[self[item + temp_coord]] += 1
        return ret

    @property
    def count_occupied(self) -> int:
        return len([seat for seat in self.values() if seat is SeatStatus.OCCUPIED])


class Ruleset:
    @staticmethod
    def apply_rule_adjacent(seat_map: SeatMap) -> SeatMap:
        new_seatmap = {}
        for location, status in seat_map.items():
            if status is not SeatStatus.FLOOR:
                neighbors = seat_map.adjacent_neighbors(location)
                if status is SeatStatus.VACANT and neighbors[SeatStatus.OCCUPIED] == 0:
                    new_seatmap[location] = SeatStatus.OCCUPIED
                elif (
                    status is SeatStatus.OCCUPIED
                    and neighbors[SeatStatus.OCCUPIED] >= 4
                ):
                    new_seatmap[location] = SeatStatus.VACANT
                else:
                    new_seatmap[location] = status
            else:
                new_seatmap[location] = status
        return SeatMap(new_seatmap)

    @staticmethod
    def apply_rule_visible(seat_map: SeatMap) -> SeatMap:
        new_seatmap = {}
        for location, status in seat_map.items():
            if status is not SeatStatus.FLOOR:
                neighbors = seat_map.visible_neighbors(location)
                if status is SeatStatus.VACANT and neighbors[SeatStatus.OCCUPIED] == 0:
                    new_seatmap[location] = SeatStatus.OCCUPIED
                elif (
                    status is SeatStatus.OCCUPIED
                    and neighbors[SeatStatus.OCCUPIED] >= 5
                ):
                    new_seatmap[location] = SeatStatus.VACANT
                else:
                    new_seatmap[location] = status
            else:
                new_seatmap[location] = status
        return SeatMap(new_seatmap)

    def apply_until_steady(
        self, seat_map: SeatMap, rulename: str, max_iterations: int = 1000
    ) -> SeatMap:
        if rulename == "adjacent":
            rule_func = self.apply_rule_adjacent
        elif rulename == "visible":
            rule_func = self.apply_rule_visible
        current_seatmap = seat_map
        for _ in range(max_iterations):
            new_seatmap = rule_func(current_seatmap)
            if new_seatmap == current_seatmap:
                return new_seatmap
            else:
                current_seatmap = new_seatmap
        raise RuntimeError(f"Did not reach steady state after {max_iterations} steps!")


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_11.txt", "r") as input_data:
        input = input_data.read().splitlines()
        seat_map = SeatMap.from_input(input)

        steady_seatmap_adjacent = Ruleset().apply_until_steady(seat_map, "adjacent")
        print(f"Part 1 Answer: {steady_seatmap_adjacent.count_occupied}")

        steady_seatmap_visible = Ruleset().apply_until_steady(seat_map, "visible")
        print(f"Part 1 Answer: {steady_seatmap_visible.count_occupied}")
