n = int(input())
mn = smn = mx = smx = None
for x in map(int, input().split()):
    if mn is None or mn > x:
        smn, mn = mn, x
    elif smn is None or smn > x:
        smn = x
    if mx is None or mx < x:
        smx, mx = mx, x
    elif smx is None or smx < x:
        smx = x
print(mn + smn, mx + smx)
