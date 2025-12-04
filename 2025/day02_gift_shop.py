def read_input(s: str | None = None) -> list[tuple[int, int]]:
    rows = []
    if s is None:
        with open("../private/2025/day02_gift_shop_input.txt", "r") as f:
            s = f.read()
    for rangetxt in s.strip().split(","):
        atxt, btxt = rangetxt.split("-")
        a, b = int(atxt), int(btxt)
        rows.append((a, b))
    return rows


def is_silly(int):
    nstr = str(int)
    halflen = len(nstr) // 2
    # Unnecessary, I think
    # if len(str) != 2*halflen:
    #     return False
    if nstr[halflen:] == nstr[:halflen]:
        return True
    return False


def is_silly2(int):
    nstr = str(int)
    for segsize in range(1, len(nstr) // 2 + 1):
        if len(nstr) % segsize != 0:
            continue
        base = nstr[:segsize]
        for i in range(2 * segsize, len(nstr) + 1, segsize):
            # Ex: if len=12 and segsize=3 then this should iterate over i=6, 9, 12
            if base != nstr[i - segsize : i]:
                break
        else:
            return True
    return False


def find_invalid_brute(ranges: list[tuple[int, int]]) -> int:
    invalidsum = 0
    for a, b in ranges:
        for n in range(a, b + 1):
            if is_silly(n):
                invalidsum += n
    return invalidsum


def find_invalid_brute2(ranges: list[tuple[int, int]]) -> int:
    invalidsum = 0
    for a, b in ranges:
        for n in range(a, b + 1):
            if is_silly2(n):
                invalidsum += n
    return invalidsum


def part1() -> int:
    input = read_input()
    return find_invalid_brute(input)


def part2() -> int:
    input = read_input()
    return find_invalid_brute2(input)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
