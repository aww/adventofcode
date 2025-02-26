def read_input(s: str = None) -> list[str]:
    rows = []
    if s is None:
        with open('../private/2024/{{full_label}}_input.txt', 'r') as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(line)
    return rows


def part1() -> int:
    return 0


def part2() -> int:
    return 0


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
