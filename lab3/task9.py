x = int(input())
ret = 0
base = 1
while x:
    ret += x % 10 * base
    x //= 10
    base *= -10
print(ret)
