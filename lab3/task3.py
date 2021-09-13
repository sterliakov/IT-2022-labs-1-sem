s = ssq = c = 0
while True:
    n = int(input())
    if n == 0:
        break
    s += n
    ssq += n**2
    c += 1
av = s / c
print(round(av, 3), round(ssq / c - av**2, 3))
