h = int(input())
w = int(input())
k = int(input())
arr = [[0 for _ in range(w)] for _ in range(h)]
for _ in range(k):
    x, y = int(input()) - 1, int(input()) - 1
    arr[x][y] = -1
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx == dy == 0
                    or x+dx < 0 or y+dy < 0
                    or x+dx >= h or y+dy >= w
                    or arr[x+dx][y+dy] == -1):
                continue
            arr[x+dx][y+dy] += 1

for row in arr:
    print(*row)
