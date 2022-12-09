from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

full_input = Path("day05").read_text()

test_input = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


@dataclass
class Move:
    num: int
    from_stack: int
    to_stack: int


Stack = List[str]


def split(raw_input: str) -> Tuple[List[Stack], List[Move]]:
    stacks_string, move_instructions = raw_input.split("\n\n")

    num_stacks = int((len(stacks_string.splitlines()[-2]) + 1) / 4)

    stacks: list[Stack] = [list() for _ in range(num_stacks)]
    for row in stacks_string.splitlines()[:-1]:
        letters = row[1::4]
        print(letters)
        for stack_idx, letter in enumerate(letters):
            if letter != " ":
                stacks[stack_idx].insert(0, letter)

    moves: list[Move] = []
    for row in move_instructions.splitlines():
        move_instruction = row.split()
        num = int(move_instruction[1])
        from_stack = int(move_instruction[3])
        to_stack = int(move_instruction[5])
        moves.append(Move(num, from_stack, to_stack))

    print(stacks)
    print(moves)
    return stacks, moves


def move_one(stacks: List[Stack], move: Move):
    for i in range(move.num):
        to_move = stacks[move.from_stack - 1].pop()
        stacks[move.to_stack - 1].append(to_move)


def move_one_groups(stacks: List[Stack], move: Move):
    to_move = stacks[move.from_stack - 1][-move.num :]
    stacks[move.from_stack - 1] = stacks[move.from_stack - 1][: -move.num]
    stacks[move.to_stack - 1].extend(to_move)


def move_all(raw_input: str) -> str:
    stacks, moves = split(raw_input)

    for move in moves:
        move_one(stacks, move)

    return "".join(stack[-1] for stack in stacks)


def move_all_groups(raw_input: str) -> str:
    stacks, moves = split(raw_input)

    for move in moves:
        move_one_groups(stacks, move)

    return "".join(stack[-1] for stack in stacks)


assert move_all(test_input) == "CMZ"

print(move_all(full_input))

assert move_all_groups(test_input) == "MCD"

print(move_all_groups(full_input))
