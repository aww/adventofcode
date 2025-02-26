import pytest
import day05_print_queue as day5


EXAMPLE_INPUT = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
EXAMPLE_RESULT = 143


def test_split_order():
    assert day5.split_order("47|53") == (47, 53)
    assert day5.split_order("97|13") == (97, 13)


def test_split_updates():
    assert (
        day5.split_update(
            """75,47,61,53,29
    """
        )
        == [75, 47, 61, 53, 29]
    )


def test_middle_number():
    assert day5.middle_number([75, 47, 61, 53, 29]) == 61
    assert day5.middle_number([97, 61, 53, 29, 13]) == 53
    assert day5.middle_number([75, 29, 13]) == 29


def test_order_check():
    rules = day5.OrderRules([(47, 13), (75, 47), (97, 75)])
    assert rules.check([75, 47, 61, 53, 29])
    assert rules.check([97, 61, 53, 29, 13])
    assert ~rules.check([75, 97, 47, 61, 53])


def test_sum_middle_correct():
    orders, updates = day5.read_input(EXAMPLE_INPUT)
    assert day5.sum_middle_correct(orders, updates) == EXAMPLE_RESULT


def test_sum_middle_corrected():
    orders, updates = day5.read_input(EXAMPLE_INPUT)
    assert day5.sum_middle_corrected(orders, updates) == 123
