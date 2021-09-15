n = int(input())
arr = [int(input()) for _ in range(n)]
d = [None for _ in arr]
d[0] = 0
if n != 1:
    d[1] = abs(arr[1] - arr[0])

    for i in range(2, n):
        d[i] = min(d[i-1] + abs(arr[i] - arr[i-1]), d[i-2] + abs(arr[i] - arr[i-2])*3)
print(d[-1])

