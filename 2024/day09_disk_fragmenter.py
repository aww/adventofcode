import collections

Block = collections.namedtuple("Block", ["pos", "len"])
Blocks = list[Block]


def read_input(s: str | None = None) -> list[int]:
    if s is None:
        with open("../private/2024/day09_disk_fragmenter_input.txt", "r") as f:
            s = f.read()
    return list(map(int, s.strip()))


def expandmap(diskmap: list[int]) -> list[int | None]:
    expanded: list[int | None] = []
    for i, n in enumerate(diskmap):
        if i % 2 == 0:
            expanded.extend([i // 2] * n)
        else:
            expanded.extend([None] * n)
    return expanded


# For Part 2 use a different encoding
def encodeblocks(diskmap: list[int]) -> tuple[Blocks, Blocks]:
    files = []
    empty = []
    position = 0
    for i, n in enumerate(diskmap):
        if i % 2 == 0:
            files.append(Block(position, n))
        else:
            if n != 0:
                empty.append(Block(position, n))
        position += n
    return files, empty


def move(expanded: list[int | None]) -> list[int | None]:
    r: list[int | None] = []
    j = len(expanded) - 1
    for i, marker in enumerate(expanded):
        if j < i:
            break  # i points at region from which file blocks were "removed"
        if marker is None:
            while (x := expanded[j]) is None:
                j -= 1
            if j <= i:
                break  # if this happens then the rest is None
            r.append(x)
            j -= 1
        else:
            r.append(marker)
    return r


# For Part 2
def moveblocks(files: Blocks, empties: Blocks) -> tuple[Blocks, Blocks]:
    files, empties = files.copy(), empties.copy()
    for i in range(len(files) - 1, -1, -1):
        for j in range(len(empties)):
            f, e = files[i], empties[j]
            if f.pos <= e.pos:
                break  # no more empty blocks before the file block
            if f.len <= e.len:
                files[i] = Block(e.pos, f.len)
                empties[j] = Block(e.pos + f.len, e.len - f.len)
                break
    return files, empties


def hash(a: list[int | None]) -> int:
    h = 0
    for i, x in enumerate(a):
        if x is not None:
            h += i * x
    return h


# For Part 2
def hashblocks(files: Blocks) -> int:
    total = 0
    for i, (position, length) in enumerate(files):
        # i * (pos + pos + 1 + ... + pos + length-1)
        total += i * ((length * position) + (length * (length - 1) // 2))
    return total


def part1() -> int:
    input = read_input()
    exp = expandmap(input)
    mv = move(exp)
    h = hash(mv)
    return h


def part2() -> int:
    input = read_input()
    files, empties = encodeblocks(input)
    files, _ = moveblocks(files, empties)
    hash = hashblocks(files)
    return hash


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
