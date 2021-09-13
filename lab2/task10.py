from itertools import groupby

curr = []
while True:
    n = int(input())
    if n == 0:
        break
    curr.append(n)
curr.sort()
for f, s in zip(curr, curr[1:]):
    if s - f == 2:
        print(f+1)
        break
else:
    print(curr[-1]+1)

