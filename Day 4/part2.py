from typing import List, Set
import re


def count_cards_recursive(copies: List[int]) -> int:
    total: int = len(copies)
    for copy in copies:
        if length := match_quant[copy]:
            total += count_cards_recursive([i for i in range(copy+1, copy+length+1)])
    return total


with open('input.txt') as f:
    lines: List[str] = f.readlines()

match_quant: List[int] = list()

for line in lines:
    res = re.search(r"(Card +\d+: )([\d ]+)(\|)([\d ]+)", line)
    winning: Set[str] = set(res[2].strip().replace("  ", " ").split(" "))
    have: Set[str] = set(res[4].strip().replace("  ", " ").split(" "))
    match_quant.append(len(have.intersection(winning)))

print(count_cards_recursive([i for i in range(len(lines))]))
