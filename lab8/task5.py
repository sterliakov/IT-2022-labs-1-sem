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


print(
    (lambda K: sum(hoar_sort([int(t)//2 + 1 for t in input().split()])[:K // 2 + 1]))(int(input()))
)
