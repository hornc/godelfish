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


def test_large_state():
    gf = '11211213030303030'
    assert gfᗒO.O(int(gf, 4), 10, 4) == 370036003500340033


def test_mandatory_arithmetic_zero():
    gf = int('112223', 4)
    assert gfᗒO.O(gf) == 0


def test_mandatory_arithmetic_288():
    gf = int('011221203', 4)
    assert gfᗒO.O(gf) == 288


def test_mandatory_arithmetic_long_zero():
    gf = int('1122120000000000000000000000000000000003', 4)
    assert gfᗒO.O(gf, 16, 3) == 0


def test_ASCII_output_in_different_bases():
    # HI = 072, 073 decimal
    # HI = 0x48, 0x49 hex
    gf = int('1121111211111111313', 4)
    dec_ = gfᗒO.O(gf, 10, 4)
    hex_ = gfᗒO.O(gf, 16, 2)
    assert dec_ != hex_
    assert dec_ == 720073
    assert hex_ == 0x4849


def test_more_ASCII():
    assert gfᗒO.O(int('112111121111111131111111113' , 4), 16, 2) == 0x4851  # H3
    assert gfᗒO.O(int('1121111211111111311111111113', 4), 16, 2) == 0x4852  # H4
    assert gfᗒO.O(int('112111121111111131111111111111111111111111111131111111331113', 4), 16, 2) == 0x48656c6c6f  # Hello


def test_hello_world():
    gf = 220004154300346839601141697640197817404810450964612631879016141088612008430732504789405572021198350571970553520586755
    assert gfᗒO.O(gf, 16, 2) == 0x48656c6c6f20776f726c64  # Hello world

