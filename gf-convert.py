#!/usr/bin/env python3
import argparse
import sys

from scripts.gfᗒbf8 import gf4_to_bf8

WHAT = """
Converts a Gödelfish number, Natural/int (𝜑̈ ∈ ℕ), or Unnatural/float (𝜑̈ ∈  (ℝ - ℕ)) to the following representations:
  * Deadfish
  * Brainfoctal
  * bf
  * Try It Online URL
"""


BF = 'brainf*'.replace('*', 'kcu'[::-1])
BF8 = ']><+-.,['


def to_deadfish(n):
    if n < 0:
        return '-' + to_deadfish(-n)
    return '0' if not n else to_deadfish(n//4).lstrip('0') + 'diso'[n%4]


def bf8_to_bf(n):
    bf8 = oct(n)[2:]
    for i,c in enumerate(BF8):
        bf8 = bf8.replace(str(i), c)
    return bf8


if __name__ == '__main__':
    all = len(sys.argv) < 3
    for i, arg in enumerate(sys.argv):
        if (arg[0] == '-') and arg[1].isdigit() and (all or arg != '-8'): sys.argv[i] = ' ' + arg  # accept negative values
    parser = argparse.ArgumentParser(description=WHAT, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--deadfish', help='convert to Deadfish', action='store_true')
    parser.add_argument('-8', '--brainfoctal', help='convert to Brainfoctal (Gödel number)', action='store_true')
    parser.add_argument('-b', '--%s' % BF, help='convert to %s' % BF, action='store_true')
    parser.add_argument('-t', '--tio', help='convert to try-it-online URL', action='store_true')
    parser.add_argument('number', help='int or float Gödel number to convert')
    args = parser.parse_args()

    n = args.number.strip()
    b = 0
    r = ''
    if '.' in n: # float
        bf8 = gf4_to_bf8(n)
        n, r = n.split('.')
        sign = n[0] if n[0] == '-' else '+'
    elif n.startswith('0d'): # custom base-4 notation
        b = 4
        n = n[2:]
    s = to_deadfish(int(n, b))
    if r:
        s += ' %s 0.%si' % (sign, r)
    else:
        bf8 = gf4_to_bf8(str(int(n, b)))

    # Output
    if all:
        print('\nDeadfish:')
    if all or args.deadfish:
        print(s)

    if all or args.brainfoctal:
        if all:
            print('\nBrainfoctal:')
        print(bf8)

    if all or getattr(args, BF):
        if all:
            print('\nbf:')
        print(bf8_to_bf(bf8))

