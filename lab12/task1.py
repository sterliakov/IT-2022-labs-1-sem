d = [[0 for _ in range(8)] for _ in range(8)]

x0, y0 = map(lambda x: int(x) - 1, input().split())
d[y0][x0] = 1

for y in range(y0, 8-1):
    for x in range(8):
        if x > 0:
            d[y+1][x-1] += d[y][x]
        if x < 7:
            d[y+1][x+1] += d[y][x]

print(sum(d[-1]))
