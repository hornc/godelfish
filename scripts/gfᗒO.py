#!/usr/bin/env python3

# Convert a Natural Gödelfish value into its resulting output encoding.
# https://esolangs.org/wiki/Gödelfish

from math import floor, log


# Final form of E (Evaluate)
E = lambda 𝜑̈, r=10, d=4: floor(O(𝜑̈, r, d)/r**d)


def I(o, c, r=10, d=4):
    # o = current output (int) 
    # c = command (int)
    # temp prevent negative:
    if o == 0 and c == 0:
        return 0
    #print('o: %d c: %d' % (o, c))
    ac = o - (o//(r**d))*r**d
    if c == 3:  # output
       return o * r**d - o + ac

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


def O(𝜑̈, r=10, d=4):
    if 𝜑̈ == 0:
        return 0
    return sum([I(O(floor(𝜑̈/(4**(floor(log(𝜑̈, 4) - i + 2)))), r, d), floor(𝜑̈/4**(floor(log(𝜑̈, 4)) - i + 1)) - (4 * floor(𝜑̈/(4**((floor(log(𝜑̈, 4)) - i + 2))))), r, d) for i in range(floor(log(𝜑̈, 4)) + 2)])


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

    o = E(value, radix, digits)

    if radix == 16:
        print(hex(o))
    elif radix == 8:
        print(oct(o))
    else:
        print(o)
