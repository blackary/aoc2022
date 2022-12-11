from __future__ import annotations
def process_line(idx, line, to_add_nums):
    if line.startswith("addx"):
        to_add_nums[idx + 2] = int(line.split(" ")[1])
    elif line.startswith("noop"):
        pass
    else:
        raise Exception("Unknown line: " + line)


def get_to_adds(instructions: str) -> list[int]:
    to_adds = [0 for _ in range(1000)]

    for idx, line in enumerate(instructions.splitlines()):
        process_line(idx, line, to_adds)

    return to_adds


def get_states(to_adds: list[int]) -> list[int]:
    states = [1 for _ in range(1000)]

    for i in range(1000):
        if i > 0:
            states[i] = states[i - 1]
        states[i] += to_adds[i]

    return states


def get_signal_strength(instructions: str) -> int:
    to_adds = get_to_adds(instructions)

    states = get_states(to_adds)

    signal_strength = 0
    for idx, state in enumerate(states[:230]):
        cycle = idx + 1
        if cycle % 20 == 0:
            #print(cycle, state, cycle * state)
            signal_strength += cycle * state

    print("HERE")
    print(states)
    print(to_adds)
    for idx, (state, to_add, instruction) in enumerate(
        zip(states, to_adds, instructions.splitlines())
    ):
        cycle = idx + 1
        print(f"{idx}\t{cycle}\t{to_add}\t{instruction}\t\t{state}\t{cycle * state}")
        if idx > 230:
            break

    return signal_strength


mini = """noop
addx 3
addx -5"""



to_adds = get_to_adds(mini)
states = get_states(to_adds)

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
assert ss == 13140
