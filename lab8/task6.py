def hoar_sort(A, depth=1, part='left'):
    if len(A) <= 1:
        return A
    else:
        barrier = A[0]
        L = []; M = []; R = []
        for elem in A:
            if elem < barrier:
                L.append(elem)
            elif elem > barrier:
                R.append(elem)
            else:
                M.append(elem)
        hoar_sort(L, depth+1, 'left')
        hoar_sort(R, depth+1, 'right')
        A[:] = L + M + R
        return A


def cmp(A, B):
    a = b = 0
    while a < len(A) and b < len(B):
        if A[a] != B[b]: return False
        while a + 1 < len(A) and A[a] == A[a+1]:
            a += 1
        while b + 1 < len(B) and B[b] == B[b+1]:
            b += 1
        a += 1; b += 1
    return A[-1] == B[-1]


input()
A = hoar_sort(input().split())
B = hoar_sort(input().split())
print('Yes' if cmp(A, B) else 'No')
