import requests
from pathlib import Path

# text = requests.get("https://adventofcode.com/2022/day/1/input").text
text = Path("input1").read_text()

lines = text.splitlines()

elves = []

elf = 0
for line in lines:
    # print(line)
    try:
        elf += int(line)
    except ValueError:
        elves.append(elf)
        elf = 0

print(max(elves))

t = sorted(elves)[-3:]
print(t)
print(sum(t))
