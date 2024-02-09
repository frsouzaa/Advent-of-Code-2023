from typing import List
import re


with open('input.txt') as f:
    content: str = f.read()

seeds: List[str] = re.findall("seeds:\s[\d\s]+", content)[0].replace("seeds: ", "").replace("\n", "").split(" ")

stages: List[List[str]] = []

for stage in re.findall("map:\s[\d\s]+", content):
    stage = stage.replace("map:", "").strip()
    stages.append([s.split(" ") for s in stage.split("\n")])

locations: List[int] = []

for seed in seeds:
    seed = int(seed)
    for stage in stages:
        for m in stage:
            if int(m[1]) <= seed < int(m[1]) + int(m[2]):
                seed = int(m[0]) - int(m[1]) + seed
                break
    locations.append(seed)

print(min(locations))
