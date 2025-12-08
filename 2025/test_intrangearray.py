import pytest
from intrangeunion import IntRangeUnion


@pytest.fixture
def exlong():
    return IntRangeUnion([23, 41, 50, 65, 68, 80])


@pytest.fixture
def exnull():
    return IntRangeUnion()


@pytest.fixture
def exshort():
    return IntRangeUnion([20, 40])


def test_long1(exlong):
    exlong.union(30, 65)
    assert exlong.aslist() == [23, 65, 68, 80]


def test_long2(exlong):
    exlong.union(30, 66)
    assert exlong.aslist() == [23, 66, 68, 80]


def test_long3(exlong):
    exlong.union(30, 67)
    assert exlong.aslist() == [23, 80]


def test_long4(exlong):
    exlong.union(30, 68)
    assert exlong.aslist() == [23, 80]


def test_long5(exlong):
    exlong.union(30, 69)
    assert exlong.aslist() == [23, 80]


def test_long6(exlong):
    exlong.union(30, 70)
    assert exlong.aslist() == [23, 80]


def test_long7(exlong):
    exlong.union(40, 65)
    assert exlong.aslist() == [23, 65, 68, 80]


def test_long8(exlong):
    exlong.union(41, 65)
    assert exlong.aslist() == [23, 65, 68, 80]


def test_long9(exlong):
    exlong.union(42, 65)
    assert exlong.aslist() == [23, 65, 68, 80]


def test_long10(exlong):
    exlong.union(43, 65)
    assert exlong.aslist() == [23, 41, 43, 65, 68, 80]


def test_edge(exnull):
    exnull.union(30, 65)
    assert exnull.aslist() == [30, 65]


def test_short1(exshort):
    exshort.union(30, 66)
    assert exshort.aslist() == [20, 66]


def test_short2(exshort):
    exshort.union(0, 30)
    assert exshort.aslist() == [0, 40]


def test_short3(exshort):
    exshort.union(0, 68)
    assert exshort.aslist() == [0, 68]


def test_short4(exshort):
    exshort.union(41, 69)
    assert exshort.aslist() == [20, 69]


def test_short5(exshort):
    exshort.union(50, 69)
    assert exshort.aslist() == [20, 40, 50, 69]


def test_area_null(exnull):
    assert exnull.area() == 0


def test_area_short(exshort):
    assert exshort.area() == 21


def test_area_long(exlong):
    assert exlong.area() == 19 + 16 + 13
