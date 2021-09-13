ret = 0
mx = None
while True:
    n = int(input())
    if n == 0:
        break
    if mx is None or mx < n:
        mx = n
        ret += 1
print(ret)
