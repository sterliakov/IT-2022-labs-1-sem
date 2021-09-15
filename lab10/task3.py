import sys
sys.setrecursionlimit(100000)

def solve(i, color):
    if i == n and arr[i] == color: return 1
    if i > n or arr[i] != color: return 0
    if cache[i] is not None:
        return cache[i]
    ret = solve(i+1, color) + solve(i+2, color)
    if colors[i] not in {color, 0}:
        ret += solve(i+1, colors[i]) + solve(i+2, colors[i])
    cache[i] = ret
    return ret


n = int(input()) - 1
arr = list(map(int, input().split()))
colors = list(map(int, input().split()))
cache = [None for _ in arr]
print(solve(0, arr[0]) % 947)

