from day15_lens_library import hashstr, hashsumseq, Hashmapper


def test_hash() -> None:
    assert hashstr("HASH") == 52


def test_hashsumseq() -> None:
    test_instr = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    assert hashsumseq(test_instr.split(',')) == 1320


def test_focusingpower() -> None:
    test_instr = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    hm = Hashmapper(test_instr.split(','))
    assert hm.focusingpower() == 145
