n = int(input())
p2 = p5 = 0

def div_pow(x, d):
    ret = 0
    while not x % d:
        x //= d
        ret += 1
    return ret

for i in range(2, n+1):
    p2 += div_pow(i, 2)
    p5 += div_pow(i, 5)

print(min(p2, p5))
