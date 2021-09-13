m = None
while True:
    n = int(input())
    if n == 0:
        break
    if m is None or m < n:
        m = n
print(m)
