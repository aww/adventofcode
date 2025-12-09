Junction = tuple[int, int, int]


def read_input(s: str | None = None) -> list[Junction]:
    rows = []
    if s is None:
        with open("../private/2025/day08_playground_input.txt", "r") as f:
            s = f.read()
    for line in s.strip().splitlines():
        line = line.strip()
        if len(line) > 0:
            x, y, z = map(int, line.split(","))
            rows.append((x, y, z))
    return rows


def wirenearestn(points: list[Junction], n) -> int:
    # Values are (dist, i, j) where i,j are all indices into points (i<j)
    # This will grow to d(d-1)/2 in length where d=len(points)
    # One could possibly make this more efficient for large d by using
    # a 3D space partioning tree.
    distances: list[tuple[int, int, int]] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distsq = 0
            for k in range(3):
                distsq += (points[i][k] - points[j][k]) * (points[i][k] - points[j][k])
            distances.append((distsq, i, j))

    # Sort by distance with closest first
    distances.sort(key=lambda x: x[0])

    # Combine the closest n pairs to form larger Circuits
    # Start everything in it's own Circuit
    circuitmembership: dict[int, list[int]] = {i: [i] for i in range(len(points))}
    for _, i, j in distances[:n]:
        if circuitmembership[i] is not circuitmembership[j]:
            circuitmembership[i].extend(circuitmembership[j])
            for k in circuitmembership[i]:
                circuitmembership[k] = circuitmembership[i]

    # Empty the dictionary to make a list of unique circuits
    uniquecircuits = []
    while len(circuitmembership) > 0:
        # Pick a random circuit that is still in circuitmembership
        nextcircuit = circuitmembership[next(iter(circuitmembership.keys()))]
        uniquecircuits.append(nextcircuit)
        for i in nextcircuit:
            del circuitmembership[i]

    # Sort the Circuits by size, largest first
    uniquecircuits.sort(key=len, reverse=True)

    # Report the product of the sizes of the three largest Circuits
    sizeproduct = 1
    for cir in uniquecircuits[:3]:
        sizeproduct *= len(cir)
    return sizeproduct


def lastconnectedprod(points: list[Junction]) -> int:
    # Similar to wirenearestn() but only stop when there is a complete circuit
    # identified by having size equal to len(points)
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distsq = 0
            for k in range(3):
                distsq += (points[i][k] - points[j][k]) * (points[i][k] - points[j][k])
            distances.append((distsq, i, j))
    distances.sort(key=lambda x: x[0])
    circuitmembership = {i: [i] for i in range(len(points))}
    for _, i, j in distances:
        if circuitmembership[i] is not circuitmembership[j]:
            circuitmembership[i].extend(circuitmembership[j])
            if len(circuitmembership[i]) == len(points):
                return points[i][0] * points[j][0]
            for k in circuitmembership[i]:
                circuitmembership[k] = circuitmembership[i]
    raise ValueError("Never reached a fully connected circuit")


def part1() -> int:
    input = read_input()
    return wirenearestn(input, 1000)


def part2() -> int:
    input = read_input()
    return lastconnectedprod(input)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
