''' Solution for O(N*M), since N and M are both very small '''
n = int(input())
colors = [tuple(int(input()) for _ in range(3)) for _ in range(n)]
m = int(input())
q_all = [int(input()) for _ in range(m)]

ret = []
for q in q_all:
    ret.append(0)
    for l, r, c in colors:
        if l <= q <= r:
            ret[-1] = c

print(*ret)
