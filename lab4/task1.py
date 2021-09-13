from math import ceil, sqrt
n = int(input())
print(1 if not any(n % i == 0 for i in range(2,1+ceil(sqrt(n)))) else 0)
