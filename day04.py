from pathlib import Path

all_days = Path("day04").read_text().splitlines()

test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def get_contains(days):
    counts = 0
    for day in days:
        first, second = day.split(",")
        f1, f2 = [int(c) for c in first.split("-")]
        s1, s2 = [int(c) for c in second.split("-")]

        if f1 <= s1 and f2 >= s2:
            counts += 1
        elif s1 <= f1 and s2 >= f2:
            counts += 1

    return counts


assert get_contains(test.splitlines()) == 2

print(get_contains(all_days))


def get_overlaps(days):
    counts = 0
    for day in days:
        first, second = day.split(",")
        f1, f2 = [int(c) for c in first.split("-")]
        s1, s2 = [int(c) for c in second.split("-")]

        if (f1 < s1 and f2 < s1) or (f1 > s2 and f2 > s2):
            counts += 0
        else:
            counts += 1

    return counts


assert get_overlaps(test.splitlines()) == 4

print(get_overlaps(all_days))
