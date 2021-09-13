def count_sort_decimals(arr):
    c = [0 for _ in range(10)]
    for el in arr:
        c[el] += 1
        print(*c)
    return sum(([i]*c[i] for i in range(10)), [])

print(*count_sort_decimals(list(map(int, input().split()))))
