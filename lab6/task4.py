def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)-i+1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                print(*arr)

bubble_sort(list(map(int, input().split())))
