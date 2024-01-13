import pytest
import itertools
import functools
import time


def parse_record(line: str) -> tuple[str, tuple]:
    record, damage_str = line.split()
    damage = tuple(map(int, damage_str.split(',')))
    return record, damage


def read_records(txt: str = None):
    if txt is None:
        with open('day12_spring_condition_input.txt', 'r') as f:
            return list(map(parse_record, f.readlines()))
    else:
        return list(map(parse_record, txt.splitlines()))


def count_arrangements_slow(record: str, damagesizes: tuple) -> int:
    # This is almost assuredly the wrong way to do this, but it should work for cases with only a few unknown values.
    # I'm betting part 2 will say question marks could indicate any number of unknowns.
    # Update: Not quite, Part 2 has everything "folded" five times, certainly making this untenable.
    nquestions = sum(c == '?' for c in record)
    count = 0
    for x in itertools.product(*(nquestions * [('.', '#')])):
        pattern = []
        iquestion = 0
        ndamage = 0
        for c in record:
            if c == '?':
                c = x[iquestion]
                iquestion += 1
            if c == '#':
                ndamage += 1
            elif c == '.' and ndamage > 0:
                pattern.append(ndamage)
                ndamage = 0
        if ndamage > 0:
            pattern.append(ndamage)
        if damagesizes == tuple(pattern):
            count += 1
    return count


def subat(s, i, c):
    return s[:i] + c + s[i+1:]


def findmiddle(s, c):
    indices = []
    lasti = -1
    while (lasti := s.find(c, lasti+1)) >= 0:
        indices.append(lasti)
    if len(indices) == 0:
        return -1
    return indices[len(indices) // 2]


@functools.cache
def count_arrangements(record: str, damagesizes: tuple) -> int:
    """The basic idea here is to either find a . in the record and split on it,
    since that must break sequences of damage.
     Or we find a ? and then try both # and . in that spot."""
    record = record.strip('.')
    if len(record) == 0 and len(damagesizes) == 0:
        return 1
    # Suppose we have damage sizes of (3,4,2) then the record must be at least 3+1+4+1+2 in length
    # corresponding to ###.####.##
    if len(record) < sum(damagesizes) + len(damagesizes) - 1:
        return 0
    # Could the following be done faster if we look the middle-most and not the first to split on?
    idot = record.find('.')
    if idot == -1:
        iquestion = record.find('?')  # findmiddle(record, '?')
        if iquestion == -1:
            # All failures (#)
            if len(damagesizes) == 1 and len(record) == damagesizes[0]:
                return 1
            else:
                return 0
        else:
            # Try both possibilities in a ? position
            return (count_arrangements(subat(record, iquestion, '.'), damagesizes)
                    + count_arrangements(subat(record, iquestion, '#'), damagesizes))
    else:
        comb = 0
        for i in range(len(damagesizes)+1):
            comb += (count_arrangements(record[:idot], damagesizes[:i])
                     * count_arrangements(record[idot+1:], damagesizes[i:]))
        return comb


def foldn(record: str, damagesizes: list, folds=5) -> tuple[str, list[int]]:
    return '?'.join(folds*[record]),  folds * damagesizes


def main():
    r = read_records()
    print(sum(count_arrangements(x[0], x[1]) for x in r))
    r = read_records()
    results = []
    for x in r:
        foldedx = foldn(*x)
        starttime = time.perf_counter()
        arrangements = count_arrangements(*foldedx)
        endtime = time.perf_counter()
        results.append({'time': endtime - starttime, 'arrangements': arrangements,
                        'record': x[0], 'damagesizes': x[1]})
    totaltime = sum(x['time'] for x in results)
    print(f"Total time: {totaltime}")
    totalarrangements = sum(x['arrangements'] for x in results)
    print(f"Total arrangements: {totalarrangements}")
    ntop = 8
    print("Top 8 slowest")
    for x in sorted(results, key=lambda x: x['time'], reverse=True)[:ntop]:
        print(x)
    # print(sum(count_arrangements(*foldn(*x)) for x in r))

if __name__ == '__main__':
    main()


@pytest.mark.parametrize(
    "record,damagesizes,answer",
    [('???.###', (1, 1, 3), 1),
     ('.??..??...?##.', (1, 1, 3), 4),
     ('?#?#?#?#?#?#?#?', (1, 3, 1, 6), 1),
     ('????.#...#...', (4, 1, 1), 1),
     ('????.######..#####.', (1, 6, 5), 4),
     ('?###????????', (3, 2, 1), 10),
     ]
)
def test_count_arrangements_slow(record, damagesizes, answer):
    assert count_arrangements_slow(record, damagesizes) == answer


@pytest.mark.parametrize(
    "record,damagesizes,answer",
    [('???.###', (1, 1, 3), 1),
     ('.??..??...?##.', (1, 1, 3), 4),
     ('?#?#?#?#?#?#?#?', (1, 3, 1, 6), 1),
     ('????.#...#...', (4, 1, 1), 1),
     ('????.######..#####.', (1, 6, 5), 4),
     ('?###????????', (3, 2, 1), 10),
     ]
)
def test_count_arrangements(record, damagesizes, answer):
    assert count_arrangements(record, damagesizes) == answer


def test_foldn():
    assert foldn('.#', [1]) == ('.#?.#?.#?.#?.#', [1, 1, 1, 1, 1])

def test_findmiddle():
    assert findmiddle('.?.', '?') == 1
    assert findmiddle('?', '?') == 0
    assert findmiddle('.?.?.?....', '?') == 3
    assert findmiddle('????????', '?') == 4
    assert findmiddle('??', '?') == 1
    assert findmiddle('    ', '?') == -1
    assert findmiddle('    ?', '?') == 4
