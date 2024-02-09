from typing import List
import re


def check_if_exists(seed: int, seeds: List[str]) -> bool:
    for i in range(0, len(seeds), 2):
        if int(seeds[i]) <= seed < int(seeds[i]) + int(seeds[i + 1]):
            return True
    return False


def get_lowest(seeds: List[str], stages: List[List[str]]) -> int:
    lowest = 0
    for i in range(0, len(seeds), 2):
        print(i)
        for j in range(int(seeds[i + 1])):
            seed = int(seeds[i]) + int(j)
            if check_if_exists(seed, seeds[:i]):
                continue
            for stage in stages:
                for m in stage:
                    if m[1] <= seed < m[3]:
                        seed = m[4] + seed
                        break
            if seed < lowest or (i == 0 and j == 0):
                print(f"menor: {seed}")
                lowest = seed
    return lowest


with open('Day 5/input.txt') as f:
    content: str = f.read()

seeds: List[str] = re.findall("seeds:\s[\d\s]+", content)[0].replace("seeds: ", "").replace("\n", "").split(" ")

stages: List[List[str]] = []

for stage in re.findall("map:\s[\d\s]+", content):
    stage = stage.replace("map:", "").strip()
    m = [[int(j) for j in i] for i in [s.split(" ") for s in stage.split("\n")]]
    for i in range(len(m)):
        m[i].append(m[i][1] + m[i][2])
        m[i].append(m[i][0] - m[i][1])
    stages.append(m)

lowest: int = get_lowest(seeds, stages)

print(lowest)
