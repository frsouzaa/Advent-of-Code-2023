from typing import List, Tuple
import re


def get_seeds(content: str) -> List[List[int]]:
    aux: List[int] = [int(i) for i in re.findall("seeds:\s[\d\s]+", content)[0].replace("seeds: ", "").replace("\n", "").split(" ")]
    seeds: List[List[int]] = []
    for i in range(0, len(aux), 2):
        seeds.append([aux[i], aux[i] + aux[i + 1] - 1, 0])
    return seeds


def get_stages(content: str) -> List[List[int]]:
    stages: List[List[int]] = []
    for stage in re.findall("map:\s[\d\s]+", content):
        stage = stage.replace("map:", "").strip()
        stages.append([[int(j) for j in i] for i in [s.split(" ") for s in stage.split("\n")]])
    return stages


def get_lowest(seeds: List[Tuple[int]], stages: List[List[int]]) -> int:
    lowest: float = float("inf")
    while seeds:
        seed = seeds.pop()
        while seed[2] < 8:
            if seed[2] == 7:
                if seed[0] < lowest:
                    lowest = seed[0]
                break
            for s in stages[seed[2]]:
                dest, source, length = s
                diff = dest - source
                if source > seed[1] or source + length - 1 < seed[0]:
                    continue
                if source <= seed[0] and source + length > seed[1]:
                    seed[0] += diff
                    seed[1] += diff
                    break
                if seed[0] >= source and seed[0] <= source + length - 1:
                    aux: List[int] = [source + length, seed[1], seed[2]]
                    seeds.append(aux)
                    seed[0] += diff
                    seed[1] = dest + length - 1
                    break
                if seed[1] >= source and seed[1] <= source + length - 1:
                    aux: List[int] = [seed[0], source - 1, seed[2]]
                    seeds.append(aux)
                    seed[0] = dest
                    seed[1] += diff
                    break
            seed[2] += 1
    return lowest


with open('input.txt') as f:
    content: str = f.read()

seeds: List[List[int]] = get_seeds(content)

stages: List[List[int]] = get_stages(content)

lowest: int = get_lowest(seeds, stages)

print(lowest)
