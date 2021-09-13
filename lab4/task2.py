from math import ceil, sqrt

def factorize(x):
    for d in range(2, 1 + ceil(sqrt(x))):
        if not x % d:
            print(d)
            factorize(x // d)
            break
    else:
        print(x)

factorize(int(input()))
