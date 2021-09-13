curr = ret = 0
mx = None

while True:
    n = int(input())
    if n == 0:
        break
    if mx is None:
        mx = n
    elif n < mx:
        ret += 1
    elif n > mx:
        ret = curr
        mx = n
    curr += 1
print(ret)
