def read_input(s: str | None = None) -> list[list[str]]:
    rows = []
    if s is None:
        with open("../private/2025/day07_laboratories_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(list(line))
    return rows


def splits(input: list[list[str]]) -> int:
    count = 0
    N = len(input)
    for i in range(N - 1):
        for j, c in enumerate(input[i]):
            if c == "S":
                input[i + 1][j] = "|"
            elif c == "|":
                if input[i + 1][j] == "^":
                    count += 1
                    input[i + 1][j - 1] = "|"
                    input[i + 1][j + 1] = "|"
                else:
                    input[i + 1][j] = "|"
    return count


# Start from the bottom and work up.
# We could skip every other line because they don't carry any information
# and aren't necessary for the algorithm, but it complicates the final c=='S' step.
# The number of ways you can go down is just the sum of the ways just below
# in each direction of a split.
def timelines(input: list[list[str]]) -> int:
    N = len(input)
    values: dict[tuple[int, int], int] = dict()
    for i in range(N - 1, -1, -1):
        for j, c in enumerate(input[i]):
            if c == "S":
                return values[(i + 1, j)]
            elif c == ".":
                if i == N - 1:
                    values[(i, j)] = 1
                else:
                    if input[i + 1][j] == "^":
                        values[(i, j)] = values[(i + 1, j - 1)] + values[(i + 1, j + 1)]
                    else:
                        values[(i, j)] = values[(i + 1, j)]
    raise ValueError("Never found S in input")


def part1() -> int:
    input = read_input()
    return splits(input)


def part2() -> int:
    input = read_input()
    return timelines(input)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
