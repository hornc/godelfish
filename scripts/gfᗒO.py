#!/usr/bin/env python3

# Convert a Natural Gödelfish value into its resulting output encoding.
# https://esolangs.org/wiki/Gödelfish

from math import floor, log


# Final Output of a Gödelfish program, excludes the current accumulator value.
O = lambda 𝜑̈, r=10, d=4: floor(E(𝜑̈, r**d)/r**d)


def I(o, c, z=10**4):
    # o = current output (int) 
    # c = command (int)
    # temp prevent negative:
    if o == 0 and c == 0:
        return 0
    #print('o: %d c: %d' % (o, c))
    ac = o - (o//(z))*z
    if c == 3:  # output
       return o * z - o + ac

    if c == 2:  # square
       v = ac**2 - ac
    if c == 1:
       #print('INC')
       v = 1
    if c == 0:
       #print('NEG')
       v = -1
    if v + ac == 256:
        return -ac
    else:
        return v


def E(𝜑̈, z=10**4):
    """
    Evaluate a Gödelfish program. Returns full state:
    current accumulator and all previous output.
    """
    if 𝜑̈ == 0:
        return 0
    return sum([I(E(floor(𝜑̈/(4**(floor(log(𝜑̈, 4) - i + 2)))), z), floor(𝜑̈/4**(floor(log(𝜑̈, 4)) - i + 1)) - (4 * floor(𝜑̈/(4**((floor(log(𝜑̈, 4)) - i + 2))))), z) for i in range(floor(log(𝜑̈, 4)) + 2)])
    #return sum([v(E(s(𝜑̈, i, 2), z) % z, d(E(s(𝜑̈, i, 2), z), c(𝜑̈, i), z)) for i in range(floor(log(𝜑̈, 4)) + 2)])

def c(𝜑̈, i):
    """ c: current Command."""
    return s(𝜑̈, i, 0) - 4 * s(𝜑̈, i, 1)

def d(x, c, z):
    """ d: Difference."""
    if c == 0:
        return -1
    elif c == 1:
        return 1
    elif c == 2:
        return (x%z)**2 - x%z
    elif c == 3:
        return x * (z - 1)

def s(𝜑̈, i, n):
    """ s: current State."""
    return floor(𝜑̈ / 4**(floor(log(𝜑̈, 4)) - i + n))

def v(a, x):
    """ v: oVerflow check.
        a = current accumulator
        x = proposed difference
    """
    if a + x < 0:
        return -a
    elif a + x == 256:
        return -a
    else:
        return a + x


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert a Natural Gödelfish value into its resulting output encoding.')
    parser.add_argument('value', help='Gödelfish value, 𝜑̈ ∈ ℕ')
    parser.add_argument('radix', help='radix of output values', nargs='?', default=10)
    parser.add_argument('digits', help='number of digits per output value in base radix', nargs='?', default=4)
    args = parser.parse_args()

    if args.value.startswith('0d'): # custom base-4 notation
        value = int(args.value[2:], 4)
    else:
        value = int(args.value)
    radix = int(args.radix)
    digits = int(args.digits)

    o = O(value, radix, digits)

    if radix == 16:
        print(hex(o))
    elif radix == 8:
        print(oct(o))
    else:
        print(o)
