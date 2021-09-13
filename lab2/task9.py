from collections import deque

d = deque()
for _ in range(6):
    d.append(int(input()))

while True:
    n = int(input())
    if n == 0:
        break
    d[1] = max(d[0], d[1])
    d.rotate(-1)
    d.append(n)

print(d.popleft())
