s = c = 0
while True:
    n = int(input())
    if n == 0:
        break
    s += n
    c += 1
print(round(s / c, 2))
