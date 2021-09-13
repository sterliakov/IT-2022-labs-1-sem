from math import ceil

n = int(input())
for a in range(1 + ceil(pow(n, 1/3))):
    try:
        bc = n - a**3
        b = round(pow(bc, 1/3))
    except TypeError:
        continue
    if b ** 3 == bc:
        print(*sorted([a, b]))
        break
else:
    print('impossible')
