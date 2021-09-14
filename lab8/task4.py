def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
    if len(A) <= 1:
        return
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

    print('depth:', depth, 'part:', part, 'array after:', A)
