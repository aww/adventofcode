def read_input(s: str | None = None) -> list[int]:
    rows = []
    if s is None:
        with open("../private/2025/day01_secret_entrance_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            if line[0] == "R":
                rows.append(int(line[1:]))
            elif line[0] == "L":
                rows.append(-int(line[1:]))
            else:
                raise ValueError(f"Unexpected direction identifier '{line[0]}'")
    return rows


def count_at_zero(rows: list[int]) -> int:
    count = 0
    pos = 50
    for r in rows:
        pos += r
        if pos % 100 == 0:
            count += 1
    return count


# Some examples
#                                                              | clks | sgn100 | newpos
# 40 + 240 -> 80 with clicks: 1 (@60) + 1 (@160)               |   2  |    2   |   80
# 40 + 260 ->  0 with clicks: 1 (@60) + 1 (@160) + 1 (@260)    |   3  |    2   |  100
# 40 + 280 -> 20 with clicks: 1 (@60) + 1 (@160) + 1 (@260)    |   3  |    2   |  120
# 40 - 220 -> 20 with clicks: 1 (@-40) + 1 (@-140)             |   2  |   -2   |   10
# 40 - 240 ->  0 with clicks: 1 (@-40) + 1 (@-140) + 1 (@-240) |   3  |   -2   |    0
# 40 - 260 -> 80 with clicks: 1 (@-40) + 1 (@-140) + 1 (@-240) |   3  |   -2   |  -20


def count_click_zero(rows: list[int]) -> int:
    count = 0
    pos = 50
    for r in rows:
        assert 0 <= pos < 100  # Verify that pos is always normalized
        if pos == 0:
            count += abs(r) // 100
            pos = r % 100
        else:
            count += abs(r) // 100
            tens = r % (100 if r > 0 else -100)  # ALT: 100 if r > 0 else -(-r % 100)
            newpos = pos + tens  # intentionally not normalized to 0-99
            if newpos <= 0 or newpos >= 100:
                count += 1
            pos = newpos % 100
    return count


def part1() -> int:
    return count_at_zero(read_input())


def part2() -> int:
    return count_click_zero(read_input())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
