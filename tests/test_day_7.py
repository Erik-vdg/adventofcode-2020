import pytest

from adventofcode_2020.day_7 import bag_definition_to_dict
from adventofcode_2020.day_7 import BagGraph


@pytest.fixture
def test_ruleset():
    return [
        "light red bags contain 1 bright white bag, 2 muted yellow bags.",
        "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
        "bright white bags contain 1 shiny gold bag.",
        "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
        "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
        "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
        "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
        "faded blue bags contain no other bags.",
        "dotted black bags contain no other bags.",
    ]


@pytest.fixture
def other_ruleset():
    return [
        "shiny gold bags contain 2 dark red bags.",
        "dark red bags contain 2 dark orange bags.",
        "dark orange bags contain 2 dark yellow bags.",
        "dark yellow bags contain 2 dark green bags.",
        "dark green bags contain 2 dark blue bags.",
        "dark blue bags contain 2 dark violet bags.",
        "dark violet bags contain no other bags.",
    ]


def test_bag_definition_to_dict():
    light_red_def = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    light_red_result = "light red", {"bright white": 1, "muted yellow": 2}

    assert bag_definition_to_dict(light_red_def) == light_red_result

    bright_white_def = "bright white bags contain 1 shiny gold bag."
    bright_white_result = "bright white", {"shiny gold": 1}

    assert bag_definition_to_dict(bright_white_def) == bright_white_result

    faded_blue_def = "faded blue bags contain no other bags."
    faded_blue_result = "faded blue", {}

    assert bag_definition_to_dict(faded_blue_def) == faded_blue_result


def test_contained_in(test_ruleset):
    bag_graph = BagGraph.from_definition_list(test_ruleset)
    found_contained_in = bag_graph.color_directly_contained_in("shiny gold")
    assert found_contained_in == {"bright white", "muted yellow"}

    completely_contained_by = bag_graph.color_completely_contained_by("shiny gold")
    assert completely_contained_by == {
        "bright white",
        "muted yellow",
        "dark orange",
        "light red",
    }


def test_contain_count(test_ruleset, other_ruleset):
    bag_graph = BagGraph.from_definition_list(test_ruleset)
    found_contain_count = bag_graph.contain_count("shiny gold")
    assert found_contain_count == 32

    bag_graph_2 = BagGraph.from_definition_list(other_ruleset)
    found_contain_count = bag_graph_2.contain_count("shiny gold")
    assert found_contain_count == 126
