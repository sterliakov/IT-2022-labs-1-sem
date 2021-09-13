'''
It's very unpythonic solution, in normal versions (3.6+ AFAIR) of python 
it should be just sorted(arr), but in 3.3 tuple comparison does something strange apparently
'''
from operator import itemgetter

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr)-i+1):
            if (arr[j][0] < arr[j-1][0]
                    or arr[j][0] == arr[j-1][0] and arr[j][1] < arr[j-1][1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]


def sum_digits(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


arr = [int(input()) for _ in range(int(input()))]
arr = [(sum_digits(x), x) for x in arr]
bubble_sort(arr)

print(*map(itemgetter(1), arr), sep='\n')
