from __future__ import annotations

from pathlib import Path


def process_line(idx, line, to_add_nums) -> int:
    if line.startswith("addx"):
        to_add = int(line.split(" ")[1])
        to_add_nums[idx + 1] = to_add
        return 2
    elif line.startswith("noop"):
        return 1
    else:
        raise ValueError("Unknown line: " + line)


def get_to_adds(instructions: str) -> list[int]:
    to_adds = [0 for _ in range(1000)]

    current_cycle = 0
    for _, line in enumerate(instructions.splitlines()):
        current_cycle += process_line(current_cycle, line, to_adds)

    return to_adds


def get_states(to_adds: list[int]) -> list[int]:
    states = [1 for _ in range(1000)]

    for i in range(1000):
        if i > 0:
            states[i] = states[i - 1]
        try:
            states[i] += to_adds[i]
        except IndexError:
            pass

    return states


def get_signal_strength(instructions: str) -> list[int]:
    to_adds = get_to_adds(instructions)

    states = get_states(to_adds)

    signal_strength = []
    for idx, state in enumerate(states[:230]):
        #cycle = idx + 1
        cycle = idx + 1
        if (cycle + 1) in [20, 60, 100, 140, 180, 220]:
        #if (cycle - 20) % 40 == 0:
            print(cycle, state, (cycle + 1) * state)
            signal_strength.append((cycle + 1) * state)

    #print("HERE")
    #print(states)
    #print(to_adds)
    print(len(states))
    print(len(to_adds))
    print(len(instructions.splitlines()))
    ii = instructions.splitlines()
    for i in range(230):
    #for idx, (state, to_add, instruction) in enumerate(
    #    zip(states, to_adds, instructions.splitlines())
    #):
        state = states[i]
        to_add = to_adds[i]
        try:
            instruction = instructions.splitlines()[i]
        except IndexError:
            instruction = ""
        cycle = i + 1
        print(f"{i}\t{cycle}\t{to_add}\t{instruction}\t\t{state}\t{cycle * state}")
        #if idx > 230:
        #    print(idx, "BREAK")
        #    break
    print("HERE")

    return signal_strength


mini = """noop
addx 3
addx -5"""



to_adds = get_to_adds(mini)
states = get_states(to_adds)

print(to_adds[:5])
print(states[:5])
assert states[:5] == [1, 1, 4, 4, -1]

sample = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


ss = get_signal_strength(sample)
print(ss)
print(sum(ss))
assert sum(ss) == 13140

ss = get_signal_strength(Path("day10").read_text())
print(sum(ss))

to_adds = get_to_adds(sample)
states = get_states(to_adds)

print(to_adds[:240])
print(states[:240])

def print_states(states):
    for idx, state in enumerate(states[:240]):
        pixel_pos = idx % 40
        if state in [pixel_pos, pixel_pos + 1, pixel_pos + 2]:
        #if pixel_pos - 2 <= state <= pixel_pos + 1:
        #if state - 1 <= pixel_pos <= state + 2:
            print("X", end="")
        else:
            print(".", end="")
        if pixel_pos == 39:
            print()

#def print_states(states):
#    for idx, state in enumerate(states):
#        print(idx, state)


print_states(states)


to_adds = get_to_adds(Path("day10").read_text())
states = get_states(to_adds)

print()
print()
print_states(states)
