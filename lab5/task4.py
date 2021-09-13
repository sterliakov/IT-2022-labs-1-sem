n = int(input())
a = list(map(int, input().split()))

ret = []
for prev, (i, el), nxt in zip(a, enumerate(a[1:], 1), a[2:]):
    if prev < el and nxt < el or prev > el and nxt > el:
        ret.append(i)

print(*ret)
