def split_barrier(A, barrier):
    if len(A) <= 1:
        return A
    else:
        L = []; M = []; R = []
        for elem in A:
            if elem < barrier:
                L.append(elem)
            elif elem > barrier:
                R.append(elem)
            else:
                M.append(elem)
        A[:] = L + M + R
        return
