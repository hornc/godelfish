import pytest
import gfᗒbf8


def original_baseline(a):
    """
    Convert gf4 into bf8 int
    """
    dfo = 0xe5969404f49930189784c48327a509f004bf8178085cb2d2809e932602cb65f85b7e26db2120bc2624193d284f8025fc0bc042
    d = 4 * 8 ** 136 + dfo
    i = 0xd8 * 8 ** 136
    s = 0x3925a69404f3d24cb2604b92d280c07c08e * 8 ** 136
    #o = 0x1c965a4a024f49324c0933d43c688204766cea0346b4804cbd5f97f864e021bec469311002f6893cd172380a309bc0690004cd41f4773e9ba9832ad90df621ec0
    o = 0x1c965a4a024f49324c0933d43cb6db6db6b74dffb43903ffd5797ac43f5d4611d1f9b21baea68ac950ffe421fcfb758007be83cf8ffe5f0ebfe1fec2308e8ded90df61fec0
    mapping = [0, i, s, o]
    return mapping[a] + d


discreet_maps = [
        gfᗒbf8.cfn,
        #gfᗒbf8.cfn_old,
        ]

cont_functions = [
        gfᗒbf8.discontinuous_piecewise_linear,
        # gfᗒbf8.cubic,
        gfᗒbf8.discontinuous_piecewise,
        ]

functions = discreet_maps + cont_functions


def test_sequence():
    b = original_baseline
    assert b(0) < b(1)
    assert b(1) < b(2)
    assert b(2) < b(3)


@pytest.mark.xfail
@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_baseline_continuous(n):
    b = original_baseline
    assert b(n) < b(n+0.5)


@pytest.mark.parametrize('fut', cont_functions)
@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_continuous(fut, n):
    assert fut(n) < fut(n + 0.5)
    assert fut(n) < fut(n + 0.0001)


@pytest.mark.parametrize('fut', functions)
@pytest.mark.parametrize('n', [0, 1, 2, 3])
def test_original_self(fut, n):
    assert fut(n) == original_baseline(n), '%s(%d) failed' % (fut.__name__, n)

