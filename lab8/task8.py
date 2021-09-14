def nxt_same_sign(arr, j):
    for i in range(j - 1, -1, -1):
        if arr[i] >= 0 and arr[j] >= 0 or arr[i] < 0 and arr[j] < 0:
            return i


def cmp(x, y):
    return x > y >= 0 or x < y < 0


def my_sort(arr):
    flag = False
    while not flag:
        flag = True
        for i in range(1, len(arr)):
            nxt = nxt_same_sign(arr, i)
            # print(i, nxt)
            if nxt is None:
                continue
            if cmp(arr[nxt], arr[i]):
                arr[nxt], arr[i] = arr[i], arr[nxt]
                print(*arr)
                flag = False


my_sort(list(map(int, input().split())))
