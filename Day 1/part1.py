from typing import List

with open("input.txt", "r") as f:
    lines: List[str] = f.readlines()

answer: int = 0

for line in lines:
    i: int = 0
    j: int = len(line) - 1
    left: int = None
    right: int = None
    while i <= j and not (left and right):
        if not left:
            if line[i].isdigit():
                left = int(line[i])
                continue
            i += 1
        if not right:
            if line[j].isdigit():
                right = int(line[j])
                continue
            j -= 1
    answer += left * 10 + right
    
print(answer)
