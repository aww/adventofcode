def read_input(s: str | None = None) -> list[str]:
    rows = []
    if s is None:
        with open("../private/2025/day04_printing_department_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(line)
    return rows


def accessible_rolls(input: list[str]) -> int:
    # A little overkill, but maybe useful in part 2,
    # we start by creating a dictionary of roll coordinates -> neighbor count;
    # then we just count entries with low neighbor counts.
    rolls: dict[tuple[int, int], int] = dict()
    for irow, row in enumerate(input):
        for icol, char in enumerate(row):
            if char == "@":
                thiscoord = (irow, icol)
                if thiscoord not in rolls:
                    rolls[thiscoord] = 0
                for prevneighbor in [
                    (irow - 1, icol - 1),
                    (irow - 1, icol),
                    (irow - 1, icol + 1),
                    (irow, icol - 1),
                ]:
                    if prevneighbor in rolls:
                        rolls[prevneighbor] += 1
                        rolls[thiscoord] += 1
    accessiblecount = 0
    for neighborcount in rolls.values():
        if neighborcount < 4:
            accessiblecount += 1
    return accessiblecount


def removable_rolls(input: list[str]) -> int:
    # Slight expansion of what we did in part 1:
    # Instead of storing neighbor counts store a list of neighbor coordinates
    rolls: dict[tuple[int, int], list[tuple[int, int]]] = dict()
    for irow, row in enumerate(input):
        for icol, char in enumerate(row):
            if char == "@":
                thiscoord = (irow, icol)
                if thiscoord not in rolls:
                    rolls[thiscoord] = []
                for prevneighbor in [
                    (irow - 1, icol - 1),
                    (irow - 1, icol),
                    (irow - 1, icol + 1),
                    (irow, icol - 1),
                ]:
                    if prevneighbor in rolls:
                        rolls[prevneighbor].append(thiscoord)
                        rolls[thiscoord].append(prevneighbor)
    # Create a list of coordinates where a roll can be removed
    to_remove = set()
    for coord, neighbors in rolls.items():
        if len(neighbors) < 4:
            to_remove.add(coord)

    removecount = 0
    while len(to_remove) > 0:
        # 1. remove all references to this roll from the neighbor rolls
        # 2. if the neighbor drops below the threshold then they are a removal candidate
        # 3. delete this roll
        coord = to_remove.pop()
        for neighbor in rolls[coord]:
            rolls[neighbor].remove(coord)
            if len(rolls[neighbor]) < 4:
                to_remove.add(neighbor)
        del rolls[coord]
        removecount += 1

    return removecount


def part1() -> int:
    input = read_input()
    return accessible_rolls(input)


def part2() -> int:
    input = read_input()
    return removable_rolls(input)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
