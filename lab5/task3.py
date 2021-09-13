from operator import itemgetter

arr = [int(input()) for _ in range(int(input()))]
d = int(input())
ret = list(map(itemgetter(0), filter(lambda x: x[1] % d == 0, enumerate(arr))))
print(*(ret if ret else [-1]))
