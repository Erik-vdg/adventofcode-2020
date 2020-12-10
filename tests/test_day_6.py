from adventofcode_2020.day_6 import count_all_sets
from adventofcode_2020.day_6 import intersect_all_sets


def test_d6_p1():
    questions = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    assert 11 == sum(count_all_sets(questions))


def test_d6_p2():
    questions = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
    assert [3, 0, 1, 1, 1] == intersect_all_sets(questions)
