from dataclasses import dataclass
from pathlib import Path
from typing import Literal, cast

from tqdm import tqdm

OperationType = Literal["+", "*", "**"]


@dataclass
class Monkey:
    id: int
    items: list[int]
    operation_type: OperationType
    operation_num: int
    test_divisible: int
    test_true_monkey: int
    test_false_monkey: int
    items_inspected: int = 0

    def throw(self, num: int, product_of_divisibles: int):
        worry = num
        if self.operation_type == "+":
            worry += self.operation_num
        elif self.operation_type == "*":
            worry *= self.operation_num
        elif self.operation_type == "**":
            worry **= self.operation_num

        #worry = int(worry / 3)
        worry = worry % product_of_divisibles

        if worry % self.test_divisible == 0:
            monkeys[self.test_true_monkey].items.append(worry)
        else:
            monkeys[self.test_false_monkey].items.append(worry)

    def throw_all(self, product_of_divisibles: int):
        for _ in range(len(self.items)):
            self.throw(self.items.pop(0), product_of_divisibles)
            self.items_inspected += 1

    @classmethod
    def from_str(cls, input_str: str) -> "Monkey":
        """
        Parse a string into a Monkey object

        Monkey 0:
            Starting items: 79, 98
            Operation: new = old * 19
            Test: divisible by 23
                If true: throw to monkey 2
                If false: throw to monkey 3
        """

        lines = [l.strip() for l in input_str.splitlines()]

        monkey_id = int(lines[0].split(" ")[1][:-1])
        items = [int(item) for item in lines[1].split(": ")[1].split(",")]
        print(lines[2].split(" "))
        operation_type = cast(OperationType, lines[2].split(" ")[4])
        try:
            operation_num = int(lines[2].split(" ")[5])
        except ValueError:
            operation_num = 2
            operation_type = "**"
        test_divisible = int(lines[3].split(" ")[3])
        test_true_monkey = int(lines[4].split(" ")[5])
        test_false_monkey = int(lines[5].split(" ")[5])

        return Monkey(
            monkey_id,
            items,
            operation_type,
            operation_num,
            test_divisible,
            test_true_monkey,
            test_false_monkey,
        )


#monkeys: dict[int, Monkey] = {}


sample = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

x = """
for monkey_str in sample.split("\n\n"):
    monkey = Monkey.from_str(monkey_str)
    monkeys[monkey.id] = monkey
"""

def print_monkeys():
    vals = []
    for monkey in monkeys:
        vals.append(f"Monkey {monkey.id}: {', '.join(str(i) for i in monkey.items)}")
    return "\n".join(vals)

#print(print_monkeys())

#for monkey in monkeys.values():
#    monkey.throw_all()

#print(print_monkeys())

x = """
for i in tqdm(range(1000)):
    for monkey in monkeys.values():
        monkey.throw_all()
    #print(print_monkeys())

inspected = [monkey.items_inspected for monkey in monkeys.values()]

s = sorted(inspected, reverse=True)

print(s[0] * s[1])
"""

monkeys: list[Monkey] = []

inputs = Path("day11").read_text().split("\n\n")



for monkey_str in inputs:
    monkey = Monkey.from_str(monkey_str)
    #monkeys[monkey.id] = monkey
    monkeys.append(monkey)

product_of_divisibles = 1
for monkey in monkeys:
    product_of_divisibles *= monkey.test_divisible

for i in tqdm(range(10000)):
    for monkey in monkeys:
        monkey.throw_all(product_of_divisibles)

inspected = [monkey.items_inspected for monkey in monkeys]
print(inspected)

s = sorted(inspected, reverse=True)

print(s[0] * s[1])
