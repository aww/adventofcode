def read_input(s: str | None = None) -> list[str]:
    rows = []
    if s is None:
        with open("../private/2025/day03_lobby_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(line)
    return rows


def max_joltage(bank: str) -> int:
    # Assumes every string contains digits 1-9 and is at least 2 characters long.

    # Step 1:
    # Find the first instance (from left) of the largest digit of the digits not last
    # This forms the largest possible tens value
    firstmax = "0"
    ifirstmax = None
    for i in range(len(bank) - 2, -1, -1):
        # We are going to be lazy and do comparisons on the characters rather
        # than integers, the ordering should be the same.
        if bank[i] >= firstmax:
            firstmax = bank[i]
            ifirstmax = i
    assert ifirstmax is not None

    # Step 2:
    # Scan for the largest digit to the right of the above digit
    secondmax = "0"
    for i in range(ifirstmax + 1, len(bank)):
        if bank[i] > secondmax:
            secondmax = bank[i]
            if secondmax == "9":  # minor optimization
                break
    return int(firstmax + secondmax)


def max_joltage_sized(bank: str, size: int) -> int:
    # The same as max_joltage but we do it recursively, find the largest digit,
    # leaving at least size-1 digits to its right.
    # Then apply the same process with the digits to the right assuming one size less.
    firstmax = "0"
    ifirstmax = None
    for i in range(len(bank) - size, -1, -1):
        if bank[i] >= firstmax:
            firstmax = bank[i]
            ifirstmax = i
    assert ifirstmax is not None

    if size == 1:
        return int(firstmax)
    submax = max_joltage_sized(bank[ifirstmax + 1 :], size - 1)
    return int(firstmax + str(submax))


def total_joltage(banks):
    sum = 0
    for bank in banks:
        sum += max_joltage(bank)
    return sum


def total_joltage_twelve(banks):
    sum = 0
    for bank in banks:
        sum += max_joltage_sized(bank, 12)
    return sum


def part1() -> int:
    input = read_input()
    return total_joltage(input)


def part2() -> int:
    input = read_input()
    return total_joltage_twelve(input)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
