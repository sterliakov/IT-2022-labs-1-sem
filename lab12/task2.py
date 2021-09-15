m, n = int(input()), int(input())
p = [[int(input()) for _ in range(n)] for _ in range(m)]
c = int(input())

d = [[0 for el in row] for row in p]
d[0][0] = c - p[0][0]
for i in range(1, n):
    d[0][i] = d[0][i-1] - p[0][i]
for y in range(1, m):
    for x in range(n):
        if x > 0:
            d[y][x] = max(d[y][x-1], d[y-1][x]) - p[y][x]
        else:
            d[y][x] = d[y-1][x] - p[y][x]

print(d[-1][-1] if d[-1][-1] >= 0 else 'Impossible')
