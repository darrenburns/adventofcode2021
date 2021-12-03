from itertools import pairwise
from typing import Iterable


def count_increases(numbers: Iterable[int]) -> int:
    return len([i for i in pairwise(numbers) if i[1] > i[0]])


def one() -> int:
    with open("input/one.txt") as f:
        numbers = [int(num) for num in f.readlines()]
    return count_increases(numbers)


def two() -> int:
    window_size = 3

    with open("input/one.txt") as f:
        nums = [int(num) for num in f.readlines()]

    triples = []
    for idx in range(len(nums) - window_size + 1):
        triples.append(nums[idx:idx + window_size])

    return count_increases(sum(t) for t in triples)


if __name__ == '__main__':
    print("Day 1, part 1: ", one())
    print("Day 1, part 2: ", two())
