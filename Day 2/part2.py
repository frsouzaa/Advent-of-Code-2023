from typing import List, Tuple
import re

with open("input.txt", "r") as f:
    lines: List[str] = f.readlines()

power_sum: int = 0

for line in lines:
    red: List[Tuple[str]] = re.findall(r"(\d+)( red)", line)
    min_red: int = max([int(i[0]) for i in red])
    
    green: List[Tuple[str]] = re.findall(r"(\d+)( green)", line)
    min_green: int = max([int(i[0]) for i in green])
    
    blue: List[Tuple[str]] = re.findall(r"(\d+)( blue)", line)
    min_blue: int = max([int(i[0]) for i in blue])

    power: int = min_red * min_green * min_blue
    power_sum += power

print(power_sum)
