import pytest
import day09_disk_fragmenter as day9

B = day9.Block


def intnone(x):
    return None if x == "." else int(x)


EXAMPLE_INPUT = """
2333133121414131402
"""
EXAMPLE_RESULT = 1928
EXAMPLE_EXPAND_TXT = "00...111...2...333.44.5555.6666.777.888899"
EXAMPLE_EXPAND = list(map(intnone, EXAMPLE_EXPAND_TXT))
EXAMPLE_MOVED = list(map(int, "0099811188827773336446555566"))

EXAMPLE_MOVED2 = list(map(intnone, "00992111777.44.333....5555.6666.....8888.."))
EXAMPLE_RESULT2 = 2858


def test_expand():
    diskmap = day9.read_input(EXAMPLE_INPUT)
    assert day9.expandmap(diskmap) == EXAMPLE_EXPAND


def test_move():
    assert day9.move(EXAMPLE_EXPAND) == EXAMPLE_MOVED


def test_hash():
    assert day9.hash(EXAMPLE_MOVED) == EXAMPLE_RESULT
    assert day9.hash(EXAMPLE_MOVED2) == EXAMPLE_RESULT2


def test_encodeblocks():
    input = day9.read_input(EXAMPLE_INPUT)
    print(input)
    files, empties = day9.encodeblocks(input)
    assert files == [
        B(0, 2),
        B(5, 3),
        B(11, 1),
        B(15, 3),
        B(19, 2),
        B(22, 4),
        B(27, 4),
        B(32, 3),
        B(36, 4),
        B(40, 2),
    ]
    assert empties == [
        B(2, 3),
        B(8, 3),
        B(12, 3),
        B(18, 1),
        B(21, 1),
        B(26, 1),
        B(31, 1),
        B(35, 1),
    ]


def test_moveblocks():
    input = day9.read_input(EXAMPLE_INPUT)
    files, empties = day9.encodeblocks(input)
    files, _ = day9.moveblocks(files, empties)
    assert files == [
        B(0, 2),
        B(5, 3),
        B(4, 1),
        B(15, 3),
        B(12, 2),
        B(22, 4),
        B(27, 4),
        B(8, 3),
        B(36, 4),
        B(2, 2),
    ]


def test_hashblocks():
    assert (
        day9.hashblocks(
            [
                B(0, 2),
                B(5, 3),
                B(4, 1),
                B(15, 3),
                B(12, 2),
                B(22, 4),
                B(27, 4),
                B(8, 3),
                B(36, 4),
                B(2, 2),
            ]
        )
        == EXAMPLE_RESULT2
    )
