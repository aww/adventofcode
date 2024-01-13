from day06_wait_for_it import read_races, ways_to_beat, ways_to_beat_fast


def test_ways_to_beat():
    races = read_races("""Time:      7  15   30
Distance:  9  40  200""")
    assert [ways_to_beat(r[0], r[1]) for r in races] == [4, 8, 9]


def test_ways_to_beat_fast():
    races = read_races("""Time:      7  15   30
Distance:  9  40  200""")
    assert [ways_to_beat_fast(r[0], r[1]) for r in races] == [4, 8, 9]
