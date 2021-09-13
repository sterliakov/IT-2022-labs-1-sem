def selection_sort(arr):
    for i in range(len(arr)-1):
        currmin = (i, arr[i])
        for k in range(i+1, len(arr)):
            if arr[k] < currmin[1]:
                currmin = (k, arr[k])
        if currmin[1] != arr[i]:
            arr[i], arr[currmin[0]] = currmin[1], arr[i]
            print(*arr)

selection_sort(list(map(int, input().split())))
