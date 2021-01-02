import pytest

from adventofcode_2020.day_11 import Coordinate
from adventofcode_2020.day_11 import Ruleset
from adventofcode_2020.day_11 import SeatMap
from adventofcode_2020.day_11 import SeatStatus


@pytest.fixture
def seat_maps():
    return {
        "initial_state": [
            "L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL",
        ],
        "expected_state_2_rules": [
            "#.LL.L#.##",
            "#LLLLLL.L#",
            "L.L.L..L..",
            "#LLL.LL.L#",
            "#.LL.LL.LL",
            "#.LLLL#.##",
            "..L.L.....",
            "#LLLLLLLL#",
            "#.LLLLLL.L",
            "#.#LLLL.##",
        ],
        "test_visible_1": [
            ".......#.",
            "...#.....",
            ".#.......",
            ".........",
            "..#L....#",
            "....#....",
            ".........",
            "#........",
            "...#.....",
        ],
        "test_visible_2": [
            ".............",
            ".L.L.#.#.#.#.",
            ".............",
        ],
        "test_visible_3": [
            ".##.##.",
            "#.#.#.#",
            "##...##",
            "...L...",
            "##...##",
            "#.#.#.#",
            ".##.##.",
        ],
    }


def test_seat_adjacent_neighbors():
    raw_map = [".L#", ".L#", ".L#"]
    seat_map = SeatMap.from_input(raw_map)
    found_neighbors = seat_map.adjacent_neighbors(Coordinate(1, 1))

    expected_neighbors = {
        SeatStatus.VACANT: 2,
        SeatStatus.OCCUPIED: 3,
        SeatStatus.FLOOR: 3,
    }
    assert found_neighbors == expected_neighbors


def test_apply_rule_adjacent(seat_maps):
    seat_map = SeatMap.from_input(seat_maps["initial_state"])

    expected_seat_map = SeatMap.from_input(seat_maps["expected_state_2_rules"])

    found_seat_map = Ruleset.apply_rule_adjacent(Ruleset.apply_rule_adjacent(seat_map))

    assert expected_seat_map == found_seat_map


def test_steady_state_adjacent(seat_maps):
    expected_occupancy_count_steady = 37
    seat_map = SeatMap.from_input(seat_maps["initial_state"])

    steady_seatmap = Ruleset().apply_until_steady(seat_map, "adjacent")

    assert expected_occupancy_count_steady == steady_seatmap.count_occupied


def test_visible_neighbors_1(seat_maps):
    seat_map = SeatMap.from_input(seat_maps["test_visible_1"])
    visible_neighbors = seat_map.visible_neighbors(Coordinate(4, 3))
    expected_vis_neighbors = {
        SeatStatus.VACANT: 0,
        SeatStatus.OCCUPIED: 8,
        SeatStatus.FLOOR: 0,
    }

    assert expected_vis_neighbors == visible_neighbors


def test_visible_neighbors_2(seat_maps):
    seat_map = SeatMap.from_input(seat_maps["test_visible_2"])
    visible_neighbors = seat_map.visible_neighbors(Coordinate(1, 1))
    expected_vis_neighbors = {
        SeatStatus.VACANT: 8,
        SeatStatus.OCCUPIED: 0,
        SeatStatus.FLOOR: 0,
    }

    assert expected_vis_neighbors == visible_neighbors


def test_visible_neighbors_3(seat_maps):
    seat_map = SeatMap.from_input(seat_maps["test_visible_3"])
    visible_neighbors = seat_map.visible_neighbors(Coordinate(3, 3))
    expected_vis_neighbors = {
        SeatStatus.VACANT: 8,
        SeatStatus.OCCUPIED: 0,
        SeatStatus.FLOOR: 0,
    }

    assert expected_vis_neighbors == visible_neighbors


def test_steady_state_visible(seat_maps):
    expected_occupancy_count_steady = 26
    seat_map = SeatMap.from_input(seat_maps["initial_state"])

    steady_seatmap = Ruleset().apply_until_steady(seat_map, "visible")

    assert expected_occupancy_count_steady == steady_seatmap.count_occupied
