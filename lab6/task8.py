def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)-i+1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [int(input()) for _ in range(int(input()))]
even = []
for i, el in enumerate(arr):
    if not el % 2:
        even.append(el)
        arr[i] = None

bubble_sort(even)

curr = 0
for i, el in enumerate(arr):
    if el is None:
        arr[i] = even[curr]
        curr += 1

print(*arr)
