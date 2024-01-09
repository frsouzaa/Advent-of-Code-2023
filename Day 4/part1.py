from typing import List, Set
import re


with open('input.txt') as f:
    lines: List[str] = f.readlines()

total_sum: int = 0

for line in lines:
    res = re.search(r"(Card +\d+: )([\d ]+)(\|)([\d ]+)", line)
    winning: Set[str] = set(res[2].strip().replace("  ", " ").split(" "))
    have: Set[str] = set(res[4].strip().replace("  ", " ").split(" "))
    if length := len(have.intersection(winning)):
        total_sum += 2**(length-1)
        
print(total_sum)
