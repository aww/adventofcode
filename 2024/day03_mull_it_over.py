import re
from collections.abc import Generator


def scan_for_muls(s: str) -> Generator[tuple[int, int], None, None]:
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", s):
        int1, int2 = int(m.group(1)), int(m.group(2))
        yield int1, int2


def scan_for_muls_do_dont(s: str) -> Generator[tuple[int, int], None, None]:
    enable = True
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)", s):
        if m.group(0)[:3] == "mul" and enable:
            int1, int2 = int(m.group(1)), int(m.group(2))
            yield int1, int2
        elif m.group(0)[:3] == "do(":
            enable = True
        elif m.group(0)[:3] == "don":
            enable = False


def sumprod(x) -> int:
    sum = 0
    for a, b in x:
        sum += a * b
    return sum


def read_input(s: str | None = None) -> str:
    if s is None:
        with open("../private/2024/day03_mull_it_over_input.txt", "r") as f:
            s = f.read()
    return s


def part1() -> int:
    s = read_input()
    return sumprod(scan_for_muls(s))


def part2() -> int:
    s = read_input()
    return sumprod(scan_for_muls_do_dont(s))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
