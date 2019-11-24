#!/usr/bin/env python3

# convert Deadfish code into Gödelfish integer
# output in various bases

import sys


REPLACE = {
        'd': '0',
        'i': '1',
        's': '2',
        'o': '3'}


def deadfish_to_gödelfish(df):
    for k,v in REPLACE.items():
        df = df.replace(k, v)
    return df


if __name__ == '__main__':

    orig = df = sys.argv[1]
    gf4 = deadfish_to_gödelfish(df)
    gf = int(gf4, 4)

    if len(sys.argv) == 2:
        print('Deadfish "%s" in Gödelfish:' % orig)
        print('    Base-4   %s₄' % gf4)
        print('    Octal  %s' % oct(gf))
        print('    Dec      %s' % gf)
        print('    Hex    %s' % hex(gf))
    elif sys.argv[2] == 'hex':
        print(hex(gf))
