"""
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""
from pathlib import Path

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

THEM = {"A": ROCK, "B": PAPER, "C": SCISSORS}
ME = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

inputs = Path("input2").read_text().splitlines()

test_inputs = """A Y
B X
C Z""".splitlines()


def get_winner(me_play: str, them_play: str) -> int:
  if me_play == them_play:
    return 3

  if me_play == ROCK:
    if them_play == PAPER:
      return 0
    elif them_play == SCISSORS:
      return 6

  if me_play == PAPER:
    if them_play == ROCK:
      return 6
    elif them_play == SCISSORS:
      return 0

  if me_play == SCISSORS:
    if them_play == ROCK:
      return 0
    elif them_play == PAPER:
      return 6


def get_score(me_letter: str, them_letter: str) -> int:
  score = 0
  me_play = ME[me_letter]
  them_play = THEM[them_letter]
  if me_play == ROCK:
    score = 1
  elif me_play == PAPER:
    score = 2
  elif me_play == SCISSORS:
    score = 3

  score += get_winner(me_play, them_play)

  return score


def get_total_score(input_lines) -> int:
  my_score = 0
  for line in input_lines:
    them_letter, me_letter = line.split(" ")
    my_score += get_score(me_letter, them_letter)
    # print(line, my_score)
  return my_score


assert get_total_score(test_inputs) == 15
assert get_total_score(["A X"]) == 1 + 3
assert get_total_score(["A Y"]) == 2 + 6
assert get_total_score(["A Z"]) == 3 + 0

assert get_total_score(["B X"]) == 1 + 0
assert get_total_score(["B Y"]) == 2 + 3
assert get_total_score(["B Z"]) == 3 + 6

assert get_total_score(["C X"]) == 1 + 6
assert get_total_score(["C Y"]) == 2 + 0
assert get_total_score(["C Z"]) == 3 + 3

print(len(inputs))
print(get_total_score(inputs))
