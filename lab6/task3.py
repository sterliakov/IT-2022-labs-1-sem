def fool_sort(arr):
    while True:
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                 arr[i-1], arr[i] = arr[i], arr[i-1]
                 print(*arr)
                 break
        else:
            break

fool_sort(list(map(int, input().split())))
