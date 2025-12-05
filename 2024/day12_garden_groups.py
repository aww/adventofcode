def read_input(s: str | None = None) -> list[list[str]]:
    rows = []
    if s is None:
        with open("../private/2024/day12_garden_groups_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(list(line))
    return rows


Position = tuple[int, int]
Region = dict[Position, int]
AreaPerim = tuple[int, int]
AreaPerimAccounting = dict[AreaPerim, int]


def accounting(a: AreaPerimAccounting) -> int:
    total = 0
    for ap, mult in a.items():
        total += ap[0] * ap[1] * mult
    return total


def findregions(chargrid: list[list[str]]) -> list[Region]:
    # All the positions on the grid with a reference to the region they are part of.
    # The region is a dict of positions and the number of their local neighbors
    regionpartners: dict[Position, dict[Position, int]] = dict()
    for irow, row in enumerate(chargrid):
        for icol, char in enumerate(row):
            pos = (irow, icol)
            for neighbor in [(irow - 1, icol), (irow, icol - 1)]:
                if (
                    neighbor in regionpartners
                    and chargrid[neighbor[0]][neighbor[1]] == char
                ):
                    if pos in regionpartners:  # already in a region
                        if regionpartners[pos] is not regionpartners[neighbor]:
                            regionpartners[pos] |= regionpartners[neighbor]  # merge
                            for n in regionpartners[pos].keys():
                                # update the rest of the neighborhood
                                regionpartners[n] = regionpartners[pos]
                        regionpartners[pos][pos] += 1
                        regionpartners[pos][neighbor] += 1
                    else:
                        region = regionpartners[neighbor]
                        region[neighbor] += 1
                        region[pos] = 1
                        regionpartners[pos] = region
            if pos not in regionpartners:  # no matching neighbors
                regionpartners[pos] = {pos: 0}
    # Now diassable regionpartners to get a list of unique regions
    regions = []
    while len(regionpartners) > 0:
        pos = next(iter(regionpartners))
        region = regionpartners[pos]
        regions.append(region)
        for neighborpos in region.keys():
            del regionpartners[neighborpos]
    return regions


def computearea(r: Region) -> int:
    return len(r)


def computeperimeter(r: Region) -> int:
    # To find the perimeter consider every element to contribute 4 units of perimeter
    # Then remove every instance that is shared.
    return 4 * len(r) - sum(r.values())


def totalprice(x: list[list[str]]) -> int:
    regions = findregions(x)
    acc: AreaPerimAccounting = dict()
    for r in regions:
        ac: AreaPerim = computearea(r), computeperimeter(r)
        if ac in acc:
            acc[ac] += 1
        else:
            acc[ac] = 1
    return accounting(acc)


def part1() -> int:
    input = read_input()
    return totalprice(input)


def part2() -> int:
    return 0


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
