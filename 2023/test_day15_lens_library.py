import pytest
import day15_lens_library as day15


def test_hash() -> None:
    assert day15.hashstr("HASH") == 52


def test_hashsumseq() -> None:
    test_instr = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    assert day15.hashsumseq(test_instr.split(',')) == 1320


def test_focusingpower() -> None:
    test_instr = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    hm = day15.Hashmapper(test_instr.split(','))
    assert hm.focusingpower() == 145


@pytest.mark.puzzle
def test_day15_part1(benchmark):
    assert benchmark(day15.part1) == 506869


@pytest.mark.puzzle
def test_day15_part2(benchmark):
    assert benchmark(day15.part2) == 271384
