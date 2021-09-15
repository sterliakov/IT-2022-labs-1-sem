#Normal solution:
#
#from functools import cache
#
#@cache
#def fib(n):
#    return fib(n-1) + fib(n-2)

n = int(input())
arr = [1, 1]


def fib(n):
    if n < len(arr):
        return arr[n]
    else:
        arr.append(fib(n-1) + fib(n-2))
        return arr[n]


print(fib(n))
