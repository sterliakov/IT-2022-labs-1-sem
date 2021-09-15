def merge(L, R, ret=None):
    if ret is None:
        ret = [None for _ in range(len(L) + len(R))]
    l = r = c = 0
    while l != len(L) and r != len(R):
        if L[l] > R[r]:
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
total = 0
curr = []
for _ in range(N):
    n = int(input())
    total += n
    curr = merge(curr, [(lambda x: (float(x[0]), x[1]))(input().split()) for _ in range(n)])

print(total)
for s, name in curr:
    print('{score:.2f} {name:s}'.format(score=s, name=name))
