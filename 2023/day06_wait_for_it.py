import math


def read_races(rr: str = None, fix_kerning=False) -> list[tuple[int, int]]:
    if rr is None:
        fn = '../private/2023/day06_boat_race_input.txt'
        with open(fn, 'r') as f:
            rr = f.read()
    line1, line2 = rr.strip().split('\n')
    label, values = line1.split(':')
    assert label == 'Time'
    if fix_kerning:
        values = values.replace(' ', '')
    times = map(int, values.split())
    label, values = line2.split(':')
    assert label == 'Distance'
    if fix_kerning:
        values = values.replace(' ', '')
    distances = map(int, values.split())

    result = zip(times, distances)
    return list(result)


def ways_to_beat(t: int, d: int) -> int:
    """t is the time for the race and d is the record distance
    A race involves charging the boat for n (integer) seconds
    and then moving at n units of speed for the remainder of the time.
    Thus pressing for n seconds sends it (t-n)*n in distance.
    So we need to find how many integers n make (t-n)*n > d.
    """
    count = 0
    for n in range(t):
        if (t-n)*n > d:
            count += 1
    return count


def ways_to_beat_fast(t: int, d: int) -> int:
    """Solve 0 > n^2 - tn + d
    [t +- sqrt(t^2 - 4d)]/2"""
    discriminant = t*t - 4*d
    if discriminant <= 0:
        return 0
    root = math.sqrt(discriminant)
    for i in range(math.floor(root), math.ceil(root)+1):
        if i*i == discriminant:
            # The discriminant is a perfect square => integer roots
            # => can't count end points (they are ties of the record)
            return i-1
    x, y = (t - math.sqrt(t*t-4*d))/2, (t + math.sqrt(t*t-4*d))/2
    # print(x, y)
    count = math.floor(y) - math.ceil(x) + 1
    # print(count)
    return count


def part1() -> int:
    races = read_races()
    # print(races)
    ways = list([ways_to_beat_fast(r[0], r[1]) for r in races])
    # print(f"Ways to beat record in each race: {ways}")
    prod = 1
    for w in ways:
        prod *= w
    return prod


def part2() -> int:
    races = read_races(None, fix_kerning=True)
    result_after_fix = ways_to_beat_fast(races[0][0], races[0][1])
    # print(f"After fixing kerning they ways are {result_after_fix}")
    return result_after_fix


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
