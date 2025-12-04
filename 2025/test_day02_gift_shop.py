import day02_gift_shop as day2


EXAMPLE_INPUT = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""
EXAMPLE_RESULT = 1227775554
EXAMPLE_RESULT_PART2 = 4174379265


def test_is_silly():
    assert day2.is_silly(55)
    assert day2.is_silly(6464)
    assert day2.is_silly(123123)
    assert not day2.is_silly(101)
    assert not day2.is_silly(1)
    assert not day2.is_silly(0)
    assert not day2.is_silly(12345)


def test_is_silly2():
    assert day2.is_silly2(55)
    assert day2.is_silly2(6464)
    assert day2.is_silly2(123123)
    assert not day2.is_silly2(101)
    assert not day2.is_silly2(1)
    assert not day2.is_silly2(0)
    assert not day2.is_silly2(12345)
    assert day2.is_silly2(12341234)
    assert day2.is_silly2(123123123)
    assert day2.is_silly2(1212121212)
    assert day2.is_silly2(1111111)
    assert not day2.is_silly2(11112)
    assert not day2.is_silly2(12121)


def test_example1():
    input = day2.read_input(EXAMPLE_INPUT)
    assert day2.find_invalid_brute(input) == EXAMPLE_RESULT
