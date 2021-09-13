def walk(arr, dir='l'):
    if len(arr) == 1:
        print(arr[0])
        return
    if dir == 'l':
        walk(arr[:-1], 'l')
    print(*arr)
    walk(arr[1:], 'r')

walk(input().split())
