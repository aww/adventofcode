from day05_if_you_give_a_seed_a_fertilizer import AlmanacTable, read_tables, map_seedranges_to_locationranges


def test_almanac_table():
    a = AlmanacTable()
    a.add_entry(50, 98, 2)
    a.add_entry(52, 50, 48)
    assert a.map(0) == 0
    assert a.map(1) == 1
    assert a.map(48) == 48
    assert a.map(50) == 52
    assert a.map(51) == 53
    assert a.map(96) == 98
    assert a.map(97) == 99
    assert a.map(98) == 50
    assert a.map(99) == 51
    assert a.map(79) == 81
    assert a.map(14) == 14
    assert a.map(55) == 57
    assert a.map(13) == 13


def test_maprange():
    a = AlmanacTable()
    a.add_entry(50, 98, 2)
    a.add_entry(52, 50, 48)
    assert a.maprange(79, 14) == [(81, 14)]
    assert a.maprange(55, 13) == [(57, 13)]
    assert a.maprange(90, 20) == [(92, 8), (50, 2), (100, 10)]


SAMPLE_TABLE_STR = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def test_full_maprange():
    seeds, tables = read_tables(SAMPLE_TABLE_STR)
    seed_ranges = []
    for i in range(len(seeds) // 2):
        seed_ranges.append((seeds[2 * i], seeds[2 * i + 1]))
    # Should I turn the list making in the following execution into
    # yields and iterators and find the min without collecting full list?
    locranges = map_seedranges_to_locationranges(seed_ranges, tables)
    minimum = min([lr[0] for lr in locranges])
    assert minimum == 46
