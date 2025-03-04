import itertools
from functools import cache


def read_input(s: str | None = None) -> list[int]:
    if s is None:
        with open("../private/2024/day11_plutonian_pebbles_input.txt", "r") as f:
            s = f.read()
    return list(map(int, s.strip().split()))


def blinkrule(x: int) -> list[int]:
    if x == 0:
        return [1]
    digitstring = str(x)
    digitlength = len(digitstring)
    if digitlength % 2 == 0:
        return [
            int(digitstring[: digitlength // 2]),
            int(digitstring[digitlength // 2 :]),
        ]
    return [x * 2024]


def blink(a: list[int]) -> list[int]:
    mapped = map(blinkrule, a)
    return list(itertools.chain.from_iterable(mapped))


@cache
def blinkcount(x: int, nblinks: int) -> int:
    if nblinks == 0:
        return 1
    return sum(blinkcount(x, nblinks - 1) for x in blinkrule(x))


def blinkcountsum(a: list[int], nblinks: int) -> int:
    return sum(blinkcount(x, nblinks) for x in a)


def part1() -> int:
    input = read_input()
    for i in range(25):
        input = blink(input)
    return len(input)


def part2() -> int:
    input = read_input()
    return blinkcountsum(input, 75)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
