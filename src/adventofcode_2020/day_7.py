import re
from typing import Dict
from typing import List
from typing import Set
from typing import Tuple

import attr


@attr.s
class BagGraph:
    adjacency_list: Dict[str, Dict[str, int]] = attr.ib()

    @classmethod
    def from_definition_list(cls, bag_rules: List[str]) -> "BagGraph":
        adjacency_list = {}
        for rule in bag_rules:
            color, edges = bag_definition_to_dict(rule)
            adjacency_list[color] = edges

        return cls(adjacency_list=adjacency_list)

    def color_directly_contained_in(self, query_color: str) -> Set[str]:
        ret_set = set()
        for found_color, rules in self.adjacency_list.items():
            if query_color in rules.keys():
                ret_set.add(found_color)
        return ret_set

    def color_completely_contained_by(self, query_color: str) -> Set[str]:
        query_set = {query_color}
        ret_set: Set[str] = set()
        new_query_set: Set[str] = set()

        while True:
            for color in query_set:
                parents = self.color_directly_contained_in(color)
                new_query_set = new_query_set.union(parents)
            ret_set = ret_set.union(new_query_set)
            if len(new_query_set) == 0:
                break
            else:
                query_set = new_query_set
                new_query_set = set()
        return ret_set

    def contain_count(self, color: str) -> int:
        ret = 0
        for found_color, num_bags in self.adjacency_list[color].items():
            ret += num_bags
            ret += num_bags * self.contain_count(found_color)
        return ret


def bag_definition_to_dict(bag_rule: str) -> Tuple[str, Dict[str, int]]:
    bag, remainder = re.split(r" bags contain ", bag_rule)
    raw_rules = re.split(r",\s", remainder)
    ret_dict = {}
    if remainder != "no other bags.":
        for rule in raw_rules:
            m = re.match(r"(?P<quantity>\d+) (?P<color>.+) bags?", rule)
            ret_dict[m.group("color")] = int(m.group("quantity"))  # type: ignore
    return bag, ret_dict


if __name__ == "__main__":
    with open("src/adventofcode_2020/input_data/day_7.txt", "r") as input_data:
        input = input_data.read().splitlines()
        bag_graph = BagGraph.from_definition_list(input)
        contained_by = bag_graph.color_completely_contained_by("shiny gold")
        print(f"Part 1: {len(contained_by)}")
        contains = bag_graph.contain_count("shiny gold")
        print(f"Part 2: {contains}")
