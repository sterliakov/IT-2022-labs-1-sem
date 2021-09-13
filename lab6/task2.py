def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = i
        while arr[curr] < arr[curr-1] and curr > 0:
            arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
            curr -= 1
            print(*arr)

insertion_sort(list(map(int, input().split())))
