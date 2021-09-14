def merge(L, R):
    ret = [0 for _ in range(len(L)+len(R))]
    l = r = c = 0
    while l != len(L) and r != len(R):
        if L[l] < R[r]:
            ret[c] = L[l]
            l += 1
        else:
            ret[c] = R[r]
            r += 1
        c += 1

    for k in range(l, len(L)):
        ret[c] = L[k]
        c += 1
    for k in range(r, len(R)):
        ret[c] = R[k]
        c += 1

    return ret
