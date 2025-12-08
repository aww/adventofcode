from intrangeunion import IntRangeUnion


def read_input(s: str | None = None) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    available = []
    if s is None:
        with open("../private/2025/day05_cafeteria_input.txt", "r") as f:
            s = f.read()
    textranges, textavailable = s.strip().split("\n\n")
    for line in textranges.strip().splitlines():
        line = line.strip()
        a, b = line.split("-")
        ranges.append((int(a), int(b)))
    for line in textavailable.strip().splitlines():
        available.append(int(line))
    return ranges, available


def countfresh(ranges, available):
    count = 0
    for id in available:
        for a, b in ranges:
            if a <= id <= b:
                count += 1
                break
    return count


def countallfresh(ranges):
    x = IntRangeUnion()
    for a, b in ranges:
        x.union(a, b)
    return x.area()


def part1() -> int:
    ranges, available = read_input()
    return countfresh(ranges, available)


def part2() -> int:
    ranges, _ = read_input()
    return countallfresh(ranges)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
