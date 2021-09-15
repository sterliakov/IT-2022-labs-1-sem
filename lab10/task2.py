import sys
sys.setrecursionlimit(100000)

def solve(i):
    if i == n: return 1
    elif i > n: return 0
    elif cache[i] is not None: return cache[i]
    elif arr[i] != 1:
        cache[i] = solve(i+1) + solve(i + arr[i])
    else:
        cache[i] = solve(i+1)
    return cache[i]

n = int(input()) - 1
arr = list(map(int, input().split()))
cache = [None for _ in arr]
print(solve(0) % 937)
