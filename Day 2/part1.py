from typing import List, Tuple
import re

MAX_RED: int = 12
MAX_GREEN: int = 13
MAX_BLUE: int = 14

with open("input.txt", "r") as f:
    lines: List[str] = f.readlines()

id_sum: int = 0

for line in lines:
    red: List[Tuple[str]] = re.findall(r"(\d+)( red)", line)
    if not all([True if int(i[0]) <= MAX_RED else False for i in red]):
        continue
    green: List[Tuple[str]] = re.findall(r"(\d+)( green)", line)
    if not all([True if int(i[0]) <= MAX_GREEN else False for i in green]):
        continue
    blue: List[Tuple[str]] = re.findall(r"(\d+)( blue)", line)
    if not all([True if int(i[0]) <= MAX_BLUE else False for i in blue]):
        continue
    index: int = int(re.search(r"(Game )(\d+)(:)", line)[2])
    id_sum += index

print(id_sum)
