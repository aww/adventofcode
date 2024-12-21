


def read_input(s: str = None) -> list[str]:
    rows = []
    if s is None:
        with open('../private/2024/day04_ceres_search_input.txt', 'r') as f:
            s = f.read()
    for line in s.splitlines():
        line = line.strip()
        if len(line) > 0:
            rows.append(line)
    return rows


def find_xmas(s: list[str]):
    sizex, sizey = len(s[0]), len(s)
    for y in range(sizey):
        for x in range(sizex):
            for d in [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]:
                searchx, searchy = x, y
                match = 'XMAS'
                i = 0
                while(True):
                    if s[searchy][searchx] == match[i]:
                        i += 1
                        if i == len(match):
                            yield x,y
                            break
                    else:
                        break  # No match
                    searchx += d[0]
                    searchy += d[1]
                    if searchx < 0 or searchx >= sizex or searchy < 0 or searchy >= sizex:
                        break  # Out of bounds

def find_x_mas(s: list[str]):
    sizex, sizey = len(s[0]), len(s)
    for y in range(1,sizey-1):
        for x in range(1, sizex-1):
            if (s[y][x] == 'A'
                and ((s[y-1][x-1] == 'M' and s[y+1][x+1] == 'S') or (s[y-1][x-1] == 'S' and s[y+1][x+1] == 'M'))
                and ((s[y+1][x-1] == 'M' and s[y-1][x+1] == 'S') or (s[y+1][x-1] == 'S' and s[y-1][x+1] == 'M'))):
                yield x,y


def part1() -> int:
    s = read_input()
    count = 0
    for x in find_xmas(s):
        count += 1
    return count


def part2() -> int:
    s = read_input()
    count = 0
    for x in find_x_mas(s):
        count += 1
    return count


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
