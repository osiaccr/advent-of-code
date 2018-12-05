#!/usr/bin/env python3

import sys

def doit(data):
    out = []
    i = 0
    while i < len(data):
        if out and data[i] != out[-1] and data[i].upper() == out[-1].upper():
            out.pop()
        else:
            out.append(data[i])
        i += 1

    return (len(out))

def main(data):
    data = [s.strip() for s in sys.stdin][0]

    lol = []
    for i in range(26):
        c = chr(ord('a') + i)
        n = list(data.replace(c, '').replace(c.upper(), ''))
        a = doit(n)
        # This print got me on the leaderboard early: about 60% of the way
        # through, one of the results was like 40% lower than the rest,
        # so I submitted it before the program finished and it was right.
        print(a)
        lol.append(a)
    print(min(lol))


if __name__ == '__main__':
    sys.exit(main(sys.argv))