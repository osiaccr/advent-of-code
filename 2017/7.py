#!/usr/bin/env python3

import sys

def check(tree, weights, root):
    if not tree[root]: return weights[root]

    kids_weights = [check(tree, weights, k) for k in tree[root]]
    right = kids_weights[0]
    if not all(w == right for w in kids_weights):
        # For my original version I didn't actually solve the problem
        # in code I just found it manually after dumping all this
        # info.
        d_weights = [weights[k] for k in tree[root]]
        #print(root, tree[root], d_weights, kids_weights)
        # This is code I wrote after to do it honestly:
        # There need to be at least 3 elements for the thing to make sense.
        sweights = sorted(kids_weights)
        wrong = sweights[0] if sweights[0] != sweights[1] else sweights[-1]
        diff = sweights[1] - wrong
        idx = kids_weights.index(wrong)
        print(d_weights[idx] + diff)

        sys.exit(0)
    return weights[root]+sum(kids_weights)


def main(args):
    data = [s.strip() for s in sys.stdin]


    things = set()
    children = set()

    tree = {}
    weights = {}
    parent = {}

    for line in data:
        # This is all like the worst string processing in the world.
        if " -> " not in line: line += " -> "
        first,last = line.split(" -> ")
        name, crap = first.split(" ")
        tops = last.split(", ")
        if tops == ['']: tops = []
        things.add(name)
        for t in tops: children.add(t)

        n = int(crap.replace("(","").replace(")",""))
        tree[name] = tops
        weights[name] = n

    root = list(things-children)[0]
    print(root)
    check(tree, weights, root)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
