def custom_binsearch(arr, el, l=0, r=None):
    if r is None: r = len(arr) - 1
	
    if r - l <= 1:
        if arr[r] == el: return r + 1
        elif arr[l] == el: return l + 1
        else: return -1

    c = (l + r) // 2
    if arr[c] >= el:
        return custom_binsearch(arr, el, l, c)
    else:
        return custom_binsearch(arr, el, c, r)


arr = list(map(int, input().split()))
k = int(input())
print(custom_binsearch(arr, k))
