import pytest
import gfᗒO


def test_commands():
    """ Test the individual commands are read correctly."""
    b4 = '12302'  # Gödelfish in base4
    gf = int(b4, 4)
    for i,c in enumerate(b4):
        assert gfᗒO.c(gf, i+1) == int(c, 4)


# Gödelfish programs in base4
cases =[
        ('1', 0),
        ('13', 1),
        ('131', 1),
        ('133', 10001),
        ('113', 2),
        ('1313', 10002),  # Multiple outputs
        ('123', 1),  # Squaring
        ('1123', 4),
        ('11123', 9),
        ('112311003', 40004),
        ('1123123', 40025),
        ]


@pytest.mark.parametrize('prog,expect', cases)
def test_basic_commands(prog, expect):
    radix = 10
    digits = 4
    assert gfᗒO.O(int(prog, 4), radix, digits) == expect


def test_no_negatives():
    gf = '1000113'
    assert gfᗒO.O(int(gf, 4)) == 2


def test_subtraction():
    gf = '11213030303030'
    assert gfᗒO.O(int(gf, 4), 10, 2) == 504030201
    assert gfᗒO.O(int(gf, 4), 10, 3) == 5004003002001
    #assert gfᗒO.O(int(gf, 4), 10, 4) == 500040003000200010000

def test_mandatory_arithmetic_zero():
    gf = int('112223', 4)
    assert gfᗒO.O(gf) == 0


def test_mandatory_arithmetic_288():
    gf = int('011221203', 4)
    assert gfᗒO.O(gf) == 288


@pytest.mark.skip("This takes too long to compute (with the current code).")
def test_mandatory_arithmetic_long_zero():
    gf = int('1122120000000000000000000000000000000003', 4)
    assert gfᗒO.O(gf, 16, 2) == 0


@pytest.mark.skip("This takes too long to compute (with the current code).")
def test_ASCII_output_in_different_bases():
    # HI = 072, 073 decimal
    # HI = 0x48, 0x49 hex
    gf = int('1121111211111111313', 4)
    dec_ = gfᗒO.O(gf, 10, 4)
    hex_ = gfᗒO.O(gf, 16, 2)
    assert dec_ != hex_
    assert dec_ == 720073
    assert hex_ == 0x4849


