from math import ceil, sqrt

def is_prime(x):
    for d in range(2, 1 + ceil(sqrt(x))):
        if not x % d:
            return False
    return True

n = int(input()) - 1
p = 2
while n:
    while not is_prime(p):
        p += 1
    n -= 1
    p += 1
print(p - 1)
