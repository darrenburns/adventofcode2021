from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Position:
    h_pos: int = 0
    depth: int = 0


@dataclass
class Submarine:
    position: Position = field(default_factory=Position)
    aim: int = 0


Command = Literal["forward", "up", "down"]


def load_commands() -> list[tuple[Command, int]]:
    with open("input/two.txt") as f:
        lines = f.readlines()
    commands = [line.split(" ") for line in lines]
    commands = [(cmd, int(num)) for [cmd, num] in commands]
    return commands


def one() -> int:
    commands = load_commands()
    submarine = Submarine()
    for command in commands:
        match command:
            case ("forward", num):
                submarine.position.h_pos += num
            case ("up", num):
                submarine.position.depth -= num
            case ("down", num):
                submarine.position.depth += num
    return submarine.position.h_pos * submarine.position.depth


def two() -> int:
    commands = load_commands()
    submarine = Submarine()
    for command in commands:
        match command:
            case ("forward", num):
                submarine.position.h_pos += num
                submarine.position.depth += submarine.aim * num
            case ("up", num):
                submarine.aim -= num
            case ("down", num):
                submarine.aim += num

    return submarine.position.h_pos * submarine.position.depth


if __name__ == '__main__':
    print("Day 2, part 1:", one())
    print("Day 2, part 2:", two())
