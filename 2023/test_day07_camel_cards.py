import pytest
from day07_camel_cards import read_cards, hand_type_key, hand_strength_key, sort_hands, score_hands
from day07_camel_cards import hand_type_joker_key, hand_strength_joker_key, sort_hands_joker
from day07_camel_cards import part1, part2


def test_read_cards():
    sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert read_cards(sample) == [
        ('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)
    ]


def test_hand_type_key():
    assert hand_type_key('32T3K') == (2, 1, 1, 1)
    assert hand_type_key('T55J5') == (3, 1, 1)
    assert hand_type_key('KK677') == (2, 2, 1)
    assert hand_type_key('KTJJT') == (2, 2, 1)
    assert hand_type_key('QQQJA') == (3, 1, 1)
    assert hand_type_key('33333') == (5,)
    assert hand_type_key('33A33') == (4, 1)


def test_hand_strength_key():
    assert hand_strength_key('32T3K') == '32a3d'
    assert hand_strength_key('T55J5') == 'a55b5'
    assert hand_strength_key('KK677') == 'dd677'
    assert hand_strength_key('KTJJT') == 'dabba'
    assert hand_strength_key('QQQJA') == 'cccbe'


def test_sort_hands():
    sample = [
        ('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)
    ]
    assert sort_hands(sample) == [
        ('32T3K', 765), ('KTJJT', 220), ('KK677', 28), ('T55J5', 684), ('QQQJA', 483),
    ]


def test_score_hands():
    sample = [('A', 765), ('B', 220), ('C', 28), ('D', 684), ('E', 483)]
    assert score_hands(sample) == 6440


def test_hand_type_joker_key():
    assert hand_type_joker_key('32T3K') == (2, 1, 1, 1)
    assert hand_type_joker_key('T55J5') == (4, 1)
    assert hand_type_joker_key('KK677') == (2, 2, 1)
    assert hand_type_joker_key('KTJJT') == (4, 1)
    assert hand_type_joker_key('QQQJA') == (4, 1)
    assert hand_type_joker_key('33333') == (5,)
    assert hand_type_joker_key('33A33') == (4, 1)


def test_hand_strength_joker_key():
    assert hand_strength_joker_key('32T3K') == '32a3d'
    assert hand_strength_joker_key('T55J5') == 'a5515'
    assert hand_strength_joker_key('KK677') == 'dd677'
    assert hand_strength_joker_key('KTJJT') == 'da11a'
    assert hand_strength_joker_key('QQQJA') == 'ccc1e'


def test_sort_hands_joker():
    sample = [
        ('32T3K', 765), ('T55J5', 684), ('KK677', 28), ('KTJJT', 220), ('QQQJA', 483)
    ]
    assert sort_hands_joker(sample) == [
        ('32T3K', 765), ('KK677', 28), ('T55J5', 684), ('QQQJA', 483), ('KTJJT', 220),
    ]


def test_score_hands_joker():
    sample = [('A', 765), ('B', 28), ('C', 684), ('D', 483), ('E', 220)]
    assert score_hands(sample) == 5905


@pytest.mark.puzzle
def test_day07_part1(benchmark):
    assert benchmark(part1) == 252656917


@pytest.mark.puzzle
def test_day07_part2(benchmark):
    assert benchmark(part2) == 253499763
