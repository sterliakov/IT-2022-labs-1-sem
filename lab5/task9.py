from bisect import bisect

input()
arr = list(map(int, input().split()))
h = [i for i, t in enumerate(arr) if t == 1]
s = [i for i, t in enumerate(arr) if t == 2]
len_s = len(s)

mx = 0
for nr in h:
    cl = bisect(s, nr)
    if cl == len_s:
        mx = max(mx, nr - s[cl - 1])
    elif cl == 0:
        mx = max(mx, s[cl] - nr)
    else:
        mx = max(mx, min(nr - s[cl-1], s[cl] - nr))
print(mx)
