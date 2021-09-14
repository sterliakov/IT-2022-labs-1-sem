from itertools import groupby
from operator import itemgetter


input()
data = []
while True:
    inp = input()
    if inp == '#':
        break

    s, m = map(int, inp.split())
    data.append((s, m))


print(*(' '.join(map(str, reversed(k[2])))
        for k in sorted([(lambda x: (sum(map(itemgetter(1), x)),
                                     list(map(lambda x: -x[0], x)),
                                     list(map(itemgetter(1), x)))
                          )(list(g))
                         for _, g in groupby(sorted(data), itemgetter(0))],
                        reverse=True)))
