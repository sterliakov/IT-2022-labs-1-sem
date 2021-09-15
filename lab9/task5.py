def bubble_sort2d(arr, N, M):
    for row in arr: print(*row)
    print()

    for i in range(1, N*M):
        for j in range(1, N*M-i+1):
            r1, c1 = (j-1) // M, (j-1) % M
            r2, c2 = j // M, j % M
            if arr[r2][c2] < arr[r1][c1]:
                arr[r2][c2], arr[r1][c1] = arr[r1][c1], arr[r2][c2]
                for row in arr: print(*row)
                print()

# if __name__ == '__main__':
#     bubble_sort2d([[0,1], [2,3]], 2, 2)

