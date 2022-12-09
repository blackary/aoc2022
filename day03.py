from pathlib import Path
from string import ascii_letters
from more_itertools import chunked

test_lines = Path("day03_test").read_text().splitlines()
lines = Path("day03").read_text().splitlines()


def get_priority(line) -> int:
    half = int(len(line) / 2)
    first, second = line[:half], line[half:]
    common_letter = list(set(first).intersection(second))[0]
    score = ascii_letters.index(common_letter) + 1
    return score


def get_priorities(lines):
    return sum(get_priority(l) for l in lines)


assert get_priorities(test_lines) == 157

print(get_priorities(lines))


def get_common(lines):
    return list(set(lines[0]).intersection(lines[1]).intersection(lines[2]))[0]


def score_groups(lines):
    score = 0
    for chunk in chunked(lines, 3):
        common = get_common(chunk)
        score += ascii_letters.index(common) + 1
    return score


print(score_groups(lines))
