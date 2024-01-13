from day04_scratchcards import get_winning_set, card_count


def test_length_winning_set():
    assert get_winning_set("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53") == {48, 83, 17, 86}
    assert get_winning_set("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19") == {32, 61}
    assert get_winning_set("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1") == {1, 21}
    assert get_winning_set("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83") == {84}
    assert get_winning_set("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36") == set()
    assert get_winning_set("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11") == set()

def test_card_count():
    assert card_count([4, 2, 2, 1, 0, 0]) == 30
