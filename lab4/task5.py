s, k = map(int, input().split())

c = ret = min(9, max(1, s - (k - 1) * 9))
s -= ret
k -= 1
while k:
    ret *= 10
    d = max(c, s - (k - 1) * 9)
    if d >= 10:
        print('impossible')
        break
    ret += d
    k -= 1
    s -= d
    if s < 0:
        print('impossible')
        break
else:
    print(ret)
