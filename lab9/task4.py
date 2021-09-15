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


def merge_sort(A):
    if len(A) == 1:
        return
    c = len(A) // 2
    L, R = A[:c], A[c:]

    merge_sort(L)
    merge_sort(R)
    merge(L, R, A)

N = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)
print((lambda x: sum(x[N//2:]) - sum(x[:N//2]))(arr))
