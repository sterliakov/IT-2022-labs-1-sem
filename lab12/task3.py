d = [[0 for _ in range(8)] for _ in range(8)]
black = [(lambda x: (ord(x[0]) - ord('a'), int(x[1]) - 1))(input()) for _ in range(int(input()))]
white = (lambda x: (ord(x[0]) - ord('a'), int(x[1]) - 1))(input())
m = [[False for _ in range(8)] for _ in range(8)]
for b in black:
   m[b[1]][b[0]] = True
d[white[1]][white[0]] = 1

for y in range(8-1):
    for x in range(8):
        if x > 0 and m[y+1][x-1]:
            d[y+1][x-1] += d[y][x]
        if x < 7 and m[y+1][x+1]:
            d[y+1][x+1] += d[y][x]
        if not m[y+1][x]:
            d[y+1][x] += d[y][x]

print(sum(d[-1]))
