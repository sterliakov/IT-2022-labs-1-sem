from operator import itemgetter

def lis(A):
    F = [0 for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(i):
            if A[j] < A[i] and F[j] > F[i]:
                F[i] = F[j]
        F[i] += 1

    return read_lis(A, F)

def read_lis(A, d):
    d = sorted(enumerate(d), key=itemgetter(1))
    currj, curr = d[-1]
    ret = [A[currj]]
    for j, x in reversed(d):
        if j < currj and x == curr - 1:
            ret.append(A[j])
            currj, curr = j, x
    return ret[::-1]
