import numpy as np
from collections import Counter


def read_input(s: str | None = None) -> tuple[list, list]:
    list1, list2 = [], []
    if s is None:
        with open("../private/2024/day01_historian_hysteria_input.txt", "r") as f:
            s = f.read()
    for line in s.splitlines():
        line = line.strip()
        if len(line) > 0:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))
    return list1, list2  # np.array([list(x) for x in lines], dtype=int)


def distance(list1, list2):
    list1.sort()
    list2.sort()
    total_distance = 0
    for a, b in zip(list1, list2):
        total_distance += abs(a - b)
    return total_distance


def part1() -> int:
    list1, list2 = read_input()
    total_distance = distance(list1, list2)
    return total_distance


def similarity(list1, list2):
    c = Counter()
    c.update(list2)
    sim_score = 0
    for num in list1:
        sim_score += num * c[num]
    return sim_score


def part2() -> int:
    list1, list2 = read_input()
    sim_score = similarity(list1, list2)
    return sim_score


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
