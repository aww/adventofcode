import day12_garden_groups as day12


EXAMPLE_INPUT1 = """
AAAA
BBCD
BBCC
EEEC
"""
EXAMPLE_INPUT2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""
EXAMPLE_INPUT3 = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

EXAMPLE_AREAPERIM1 = {(4, 10): 2, (4, 8): 1, (1, 4): 1, (3, 8): 1}
EXAMPLE_RESULT1 = 140
EXAMPLE_AREAPERIM2 = {(1, 4): 4, (21, 36): 1}
EXAMPLE_RESULT2 = 772
EXAMPLE_AREAPERIM3 = {
    (12, 18): 1,
    (4, 8): 1,
    (14, 28): 1,
    (10, 18): 1,
    (13, 20): 1,
    (11, 20): 1,
    (1, 4): 1,
    (13, 18): 1,
    (14, 22): 1,
    (14, 22): 1,
    (5, 12): 1,
    (3, 8): 1,
}
EXAMPLE_RESULT3 = 1930


def test_accounting():
    assert day12.accounting(EXAMPLE_AREAPERIM1) == EXAMPLE_RESULT1
    assert day12.accounting(EXAMPLE_AREAPERIM2) == EXAMPLE_RESULT2
    assert day12.accounting(EXAMPLE_AREAPERIM3) == EXAMPLE_RESULT3


def test_totalprice():
    input1 = day12.read_input(EXAMPLE_INPUT1)
    assert day12.totalprice(input1) == EXAMPLE_RESULT1
    input2 = day12.read_input(EXAMPLE_INPUT2)
    assert day12.totalprice(input2) == EXAMPLE_RESULT2
    input3 = day12.read_input(EXAMPLE_INPUT3)
    assert day12.totalprice(input3) == EXAMPLE_RESULT3
