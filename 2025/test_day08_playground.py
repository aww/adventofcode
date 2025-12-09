import day08_playground as day8


EXAMPLE_INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
EXAMPLE_RESULT = 40
EXAMPLE_RESULT_PART2 = 25272


def test_wirenearestn():
    input = day8.read_input(EXAMPLE_INPUT)
    assert day8.wirenearestn(input, 10) == EXAMPLE_RESULT


def test_lastconnectedprod():
    input = day8.read_input(EXAMPLE_INPUT)
    assert day8.lastconnectedprod(input) == EXAMPLE_RESULT_PART2
