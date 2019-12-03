#!/usr/bin/env python3

# Convert a Gödelfish integer into Brainfoctal
# https://esolangs.org/wiki/Gödelfish
# https://esolangs.org/wiki/Brainfoctal

from decimal import *
import math

gfsize = lambda n: int(math.floor(math.log(n, 4)) + 1)
bfsize = lambda n: int(math.floor(math.log(n, 8)) + 1)

dfo = 0xe5969404f49930189784c48327a509f004bf8178085cb2d2809e932602cb65f85b7e26db2120bc2624193d284f8025fc0bc042
d = 4 * 8 ** 136 + dfo 
D_CONST = d

def cfn_old(a):
    # convert 0-3 into fake bf8
    bf_o = 0x1c965a4a024f49324c0933d43cb6db6db6bc3396483df8990592124903e06db6dbe9b6db301e932603d264c09021784b6db6df4db6d9802f7c082
    bf_s = 0x3925a69404f3d24cb2604b92d280c07c092
    return a + 2 + ((not a) * (bf_o - 2)) + ((a & 2)>>1 & (a & 1)) * (bf_s - 5)


def cfn(x):
    return continuous_piecewise_linear(x)

def cfn_mapped(a):
    """
    Convert gf4 into bf8 int, via piecewise linear fn
    """
    i = 0xd8 * 8 ** 136
    #s = 0x3925a69404f3d24cb2604b92d280c07c092 * 8 ** 136
    s = 0x3925a69404f3d24cb2604b92d280c07c08e * 8 ** 136
    #o = 0x1c965a4a024f49324c0933d43c688204766cea0346b4804cbd5f97f864e021bec469311002f6893cd172380a309bc0690004cd41f4773e9ba9832ad90df621ec0
    o = 0x1c965a4a024f49324c0933d43cb6db6db6b74dffb43903ffd5797ac43f5d4611d1f9b21baea68ac950ffe421fcfb758007be83cf8ffe5f0ebfe1fec2308e8ded90df61fec0 
    mapping = [0, i, s, o]
    return mapping[a] + d


def discontinuous_piecewise_linear(x):
    if x < 2:
        return di_linear(x)
    else:
        return so_linear(x)


def di_linear(x):
    i = 0xd8 * 8 ** 136
    return D_CONST + x * i


def so_linear(x):
    o = 0x1903ffe0c2000c0d80e32f1b0f8ecf65f6294dffb43903ffd5797ac43f5d4611d1f9b21baea68ac950ffe421fcfb758007be83cf8ffe5f0ebfe1fec2308e8ded90df61fec0
    g = 0x2e75a55843b0daf636a0597cf1f592c42bbfb668d46d13667ada5e03ba37647e9a035f77dbd50d35ef2d47a566d0e834a984ac20f9219cfcc39dd96b23f4cc5afbc2b83d3e
    return x * o - g


def continuous_piecewise_linear(x):
    # current best!!
    return max(di_linear(x), so_linear(x))

    # old version where the crossover ~= 1.9
    if x < 1.9:
        return di_linear(x)
    else:
        return so_linear(x)

def discontinuous_piecewise(x):
    if x < 2:
        i = 0xd8 * 8 ** 136
        s = 0x3925a69404f3d24cb2604b92d280c07c08e * 8 ** 136
        return i * x**3 + D_CONST
    else:
        return so_linear(x)

def cubic(x):
    i = 0xd8 * 8 ** 136
    s = 0x3925a69404f3d24cb2604b92d280c07c08e * 8 ** 136
    h = 0
    return i * (x - h)**3 + D_CONST

def ith_gf4(φ̈, i):
    """
    Return the ith base-4 digit of φ̈
    """
    return (φ̈//(4**i)%4)


def abs_bf8of1gf4(a, n):
    """
    bf8 of nth gf4
    """
    return cfn(ith_gf4(a, n)) * 8 ** sum([bfsize(cfn(ith_gf4(a, i))) for i in range(n)])


def gf4_to_bf8(gf4):
    """
    Converts a Gödelfish number to Brainfoctal.

    :param gf4: Gödelfish value.
    :type gf4: str
    :rtype: int
    """
    if '.' in gf4:
        getcontext().prec = 300
        gf4 = Decimal(gf4)
    else:
        gf4 = int(gf4, 0)

    if gf4 == 0 or gf4 % 1:
        #  Unatural, return single value from the function
        return int(cfn(gf4))
    # Natural, return the mod 4 compound result
    return sum([abs_bf8of1gf4(gf4, n) for n in range(gfsize(gf4))])


if __name__ == '__main__':
    import sys
    value = sys.argv[1]
    print(gf4_to_bf8(value)) 
