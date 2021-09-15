EPS = 1e-6

def find_root(func, a, b, tol):
    while b - a >= tol or abs(func(c)) >= EPS:
        c = (a + b) / 2
        if func(c) * func(a) <= 0:
            b = c
        else:
            a = c
    return (a+b) / 2
