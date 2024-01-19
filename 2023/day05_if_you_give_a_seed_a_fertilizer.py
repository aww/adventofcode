import re


class AlmanacTable:
    def __init__(self):
        self._table = []

    def add_entry(self, dst: int, src: int, length: int) -> None:
        self._table.append({'source': src, 'destination': dst, 'length': length})

    def map(self, src: int) -> int:
        """Map a source (src) to a destination"""
        for row in self._table:
            if row['source'] <= src < row['source'] + row['length']:
                return row['destination'] + src - row['source']
        return src

    def maprange(self, start: int, length: int) -> list[tuple[int, int]]:
        result = []
        point = start
        length_remaining = length
        while True:
            # Find the source range in the table where the point sits
            # and find the largest range that can be mapped before running out
            # (of either the range in the table or the range being mapped).
            for row in self._table:
                if row['source'] <= point < row['source'] + row['length']:
                    maxstep = min(row['length'] - (point - row['source']), length_remaining)
                    result.append((row['destination'] + point - row['source'], maxstep))
                    point += maxstep
                    length_remaining -= maxstep
                    break
            else:
                # The current point doesn't fall in any range, an identity mapping happens,
                # but now we need to search to find out if the mapping eventually intersects
                # a source range in the table.
                lowest = None
                for row in self._table:
                    if point < row['source'] and (lowest is None or row['source'] < lowest):
                        lowest = row['source']
                if lowest is None:
                    # No intersection
                    result.append((point, length_remaining))
                    length_remaining = 0
                else:
                    maxstep = min(lowest - point, length_remaining)
                    result.append((point, maxstep))
                    length_remaining -= maxstep
                # Now lowest
            if length_remaining <= 0:
                break
        return result

    def mapranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        result = []
        for r in ranges:
            result.extend(self.maprange(r[0], r[1]))
        return result


def read_tables(almanac_text: str = None) -> (list[int], dict[str, AlmanacTable]):
    if almanac_text is None:
        with open('../private/2023/day05_almanac_input.txt', 'r') as f:
            almanac_text = f.read()
    almanac_sections = almanac_text.split('\n\n')
    seeds = []
    tables = {}
    for sec in almanac_sections:
        label, text_table = sec.split(':')
        if label == 'seeds':
            seeds.extend(map(int, text_table.strip().split()))
        elif m := re.match(r'(.*) map$', label):
            name = m.group(1)
            tables[name] = AlmanacTable()
            for line in text_table.strip().split('\n'):
                dst, src, length = map(int, line.split())
                tables[name].add_entry(dst, src, length)
    return seeds, tables


def map_seed_to_location(seed, tables) -> int:
    soil = tables['seed-to-soil'].map(seed)
    fert = tables['soil-to-fertilizer'].map(soil)
    water = tables['fertilizer-to-water'].map(fert)
    light = tables['water-to-light'].map(water)
    temp = tables['light-to-temperature'].map(light)
    humi = tables['temperature-to-humidity'].map(temp)
    loc = tables['humidity-to-location'].map(humi)
    return loc


def map_seedranges_to_locationranges(seedranges, tables) -> list[tuple[int, int]]:
    soilranges = tables['seed-to-soil'].mapranges(seedranges)
    fertranges = tables['soil-to-fertilizer'].mapranges(soilranges)
    waterranges = tables['fertilizer-to-water'].mapranges(fertranges)
    lightranges = tables['water-to-light'].mapranges(waterranges)
    tempranges = tables['light-to-temperature'].mapranges(lightranges)
    humiranges = tables['temperature-to-humidity'].mapranges(tempranges)
    locranges = tables['humidity-to-location'].mapranges(humiranges)
    return locranges


def part1() -> int:
    seeds, tables = read_tables()
    # print(f"Number of seeds: {len(seeds)}")
    # for t in tables:
    #     print(f"Table: {t}")

    locs = []
    for s in seeds:
        loc = map_seed_to_location(s, tables)
        locs.append(loc)
        # print(f"Seed {s} maps to location {loc}")
    return min(locs)


def part2() -> int:
    seeds, tables = read_tables()
    assert len(seeds) % 2 == 0
    seed_ranges = []
    for i in range(len(seeds) // 2):
        seed_ranges.append((seeds[2*i], seeds[2*i+1]))
    # seed_range_len = sum([x[1] for x in seed_ranges])
    # print(f"Found {len(seed_ranges)} seed ranges of total length {seed_range_len}")
    locranges = map_seedranges_to_locationranges(seed_ranges, tables)
    # loc_range_len = sum([x[1] for x in locranges])
    # print(f"Found {len(locranges)} location ranges of total length {loc_range_len}")
    minimum = min([lr[0] for lr in locranges])
    return minimum


if __name__ == '__main__':
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
