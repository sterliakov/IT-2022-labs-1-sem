def sol(k, m):
    return k if m == 1 else 2 * k + sol(k+1, m-1)

print(sol(int(input()), int(input())))

