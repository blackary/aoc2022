from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Move:
    direction: str
    num: int

    @staticmethod
    def from_string(raw_move: str) -> Move:
        direction = raw_move.split(" ")[0]
        num = int(raw_move.split(" ")[1])

        return Move(direction, num)


@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int

    def move(self, move: Move):
        if move.direction == "U":
            self.y += move.num
        elif move.direction == "D":
            self.y -= move.num
        elif move.direction == "L":
            self.x -= move.num
        elif move.direction == "R":
            self.x += move.num
        else:
            raise ValueError(f"Unknown direction {move.direction}")

    def delta(self, other: "Position") -> "Position":
        return Position(self.x - other.x, self.y - other.y)

    @property
    def size(self) -> int:
        return abs(self.x) + abs(self.y)

    def distance(self, other: "Position") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def are_adjacent(self, other: "Position") -> bool:
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    @property
    def direction(self) -> "Position":
        try:
            x_dir = int(self.x / abs(self.x))
        except ZeroDivisionError:
            x_dir = 0

        try:
            y_dir = int(self.y / abs(self.y))
        except ZeroDivisionError:
            y_dir = 0

        return Position(x_dir, y_dir)

    @property
    def moves(self) -> list[Move]:
        moves = []
        if self.x != 0:
            moves.append(Move("R" if self.x > 0 else "L", abs(self.x)))
        if self.y != 0:
            moves.append(Move("U" if self.y > 0 else "D", abs(self.y)))
        return moves


def needed_moves(t_pos: Position, h_pos: Position) -> list[Move]:
    delta = h_pos.delta(t_pos)

    if t_pos.are_adjacent(h_pos):
        return []

    return delta.direction.moves


def move(pos: Position, move: Move):
    pos.move(move)


# def print_positions(t_pos: Position, h_pos: Position):
def print_positions(
    positions: Iterable[Position], symbols: Iterable[str], size: int = 10
):
    """
    Print t and h positions on a 10 x 10 grid
    """

    grid = [["." for _ in range(10)] for _ in range(10)]

    for pos, symbol in zip(positions, symbols):
        grid[pos.y][pos.x] = symbol

    for row in grid:
        print("".join(row))


def print_all_positions(
    positions: Iterable[Position], symbols: list[str], size: int = 10
):
    """
    Print all positions on a 10 x 10 grid
    """

    grid = [["." for _ in range(size)] for _ in range(size)]

    for pos, symbol in zip(positions, symbols):
        try:
            grid[pos.y][pos.x] = symbol
        except IndexError:
            pass

    for row in grid:
        print("".join(row))


sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def get_total_positions(raw_input: str, size=10) -> int:
    t_pos = Position(0, 0)
    h_pos = Position(0, 0)

    t_positions: set[Position] = set([t_pos])

    for raw_h_move in raw_input.splitlines():
        h_move = Move.from_string(raw_h_move)
        for _ in range(h_move.num):
            move(h_pos, Move(h_move.direction, 1))
            t_moves = needed_moves(t_pos, h_pos)
            for t_move in t_moves:
                move(t_pos, t_move)
            if t_pos not in t_positions:
                t_positions.add(deepcopy(t_pos))
            #print_positions([t_pos, h_pos], ["T", "H"])
            #print_all_positions([t_pos, h_pos], ["T", "H"], size=size)

    # print(t_positions)

    print_all_positions(t_positions, ["S"] * len(t_positions), size=size)

    return len(t_positions)


assert get_total_positions(sample) == 13

input = Path("day09").read_text()

print(get_total_positions(input, size=100))


def get_total_positions_n(raw_input: str, n_tails: int=9, grid_size=10) -> int:
    #t_pos = Position(0, 0)
    #h_pos = Position(0, 0)
    tails = [Position(0, 0) for _ in range(n_tails + 1)]

    t_positions: set[Position] = set([tails[-1]])

    for raw_h_move in raw_input.splitlines():
        h_move = Move.from_string(raw_h_move)
        for _ in range(h_move.num):
            move(tails[0], Move(h_move.direction, 1))

            for idx, (t_head, t_tail) in enumerate(zip(tails[:-1], tails[1:])):
                t_moves = needed_moves(t_tail, t_head)
                for t_move in t_moves:
                    move(t_tail, t_move)
                if idx == n_tails-1 and t_tail not in t_positions:
                    t_positions.add(deepcopy(t_tail))
            #print_all_positions(tails, list(map(str, range(len(tails)))), size=grid_size)
            #print_positions([t_pos, h_pos], ["T", "H"])
            #print_all_positions([t_pos, h_pos], ["T", "H"], size=size)

    # print(t_positions)

    print_all_positions(t_positions, ["S"] * len(t_positions), size=grid_size)

    return len(t_positions)


sample2a = """R 5
U 8"""
sample2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

assert get_total_positions_n(sample2, n_tails=9, grid_size=100) == 36

print(get_total_positions_n(input, n_tails=9, grid_size=100))