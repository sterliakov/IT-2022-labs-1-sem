def custom_binsearch(arr, el):
    l, r = 0, len(arr) - 1
    while r - l > 1:
        c = (l + r) // 2
        if arr[c] >= el:
            r = c
        if arr[c] <= el:
            l = c
    if arr[l] == el: return l + 1
    elif arr[r] == el: return r + 1
    return -1


input()
k = int(input())
arr = list(map(int, input().split()))
print(custom_binsearch(arr, k))
