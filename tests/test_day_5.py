from adventofcode_2020.day_5 import Seat


def test_seat():
    assert Seat.from_boarding_pass("FBFBBFFRLR") == Seat(44, 5)
    assert Seat.from_boarding_pass("BFFFBBFRRR") == Seat(70, 7)
    assert Seat.from_boarding_pass("FFFBBBFRRR") == Seat(14, 7)
    assert Seat.from_boarding_pass("BBFFBBFRLL") == Seat(102, 4)
