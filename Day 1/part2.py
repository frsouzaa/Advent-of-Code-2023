from typing import List, Dict

string_to_number: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

with open("input.txt", "r") as f:
    lines: List[str] = f.readlines()

answer: int = 0

for line in lines:
    left_positions: Dict[int, str] = dict()
    right_positions: Dict[int, str] = dict()
    for string in string_to_number:
        if (index := line.find(string)) > -1:
            left_positions[index] = string
        if (index := line.rfind(string)) > -1:
            right_positions[index] = string
    left: int = string_to_number[left_positions[min(left_positions)]]
    right: int = string_to_number[right_positions[max(right_positions)]]
    answer += left * 10 + right

print(answer)
