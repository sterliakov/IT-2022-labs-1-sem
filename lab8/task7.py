def min_index( a , i , j ):
    if i == j:
        return i
    k = min_index(a, i + 1, j)
    return (i if a[i] < a[k] else k)

def my_sort(a, n=None, index = 0):
    if n is None:
        n = len(a)
    if index == n:
        return -1

    k = min_index(a, index, n-1)
    if k != index:
        a[k], a[index] = a[index], a[k]
        print(*a)
    my_sort(a, n, index + 1)

my_sort(list(map(int, input().split())))
