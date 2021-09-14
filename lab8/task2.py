def merge(L, R, ret):
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


def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)

    if len(A) == 1:
        return
    c = len(A) // 2
    L, R = A[:c], A[c:]

    merge_sort(L, depth + 1, 'left')
    merge_sort(R, depth + 1, 'right')
    merge(L, R, A)

    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)
