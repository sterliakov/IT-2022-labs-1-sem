import sys
sys.setrecursionlimit(100000)

n = int(input())

d = [[None for _ in range(n)] for _ in range(3)]


def solve(rem, dang=0):
    if rem == 0:
        return 1
    if d[dang][rem - 1] is not None:
        return d[dang][rem - 1]
    if dang < 2:
        d[dang][rem - 1] = solve(rem - 1, 0) + solve(rem - 1, dang + 1)
    else:
        d[dang][rem - 1] = solve(rem - 1, 0)
    return d[dang][rem - 1]


print(solve(n))
