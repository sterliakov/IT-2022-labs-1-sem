from operator import itemgetter
c = [0, 0, 0, 0]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x > 0 and y > 0: c[0] += 1
    elif x > 0 and y < 0: c[3] += 1
    elif x < 0 and y < 0: c[2] += 1
    elif x < 0 and y > 0: c[1] += 1
print(*max(enumerate(c, 1), key=itemgetter(1)))
