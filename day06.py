from pathlib import Path


def count_start(datastream: str, n_chars: int = 4) -> int:
    for idx in range(len(datastream) - n_chars):
        chars = datastream[idx : idx + n_chars]
        if len(set(chars)) == n_chars:
            return idx + n_chars
    raise ValueError("No start found")


assert count_start("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert count_start("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert count_start("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert count_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert count_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

input = Path("day06").read_text()

print(count_start(input))

assert count_start("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
assert count_start("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert count_start("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
assert count_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
assert count_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

print(count_start(input, 14))
