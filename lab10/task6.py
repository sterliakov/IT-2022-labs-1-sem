# 1 | 4 | 7 | 10 | 13 | 16...
# 2 | 5 | 8 | 11 | 14 | 17...
# 3 | 6 | 9 | 12 | 15 | 18...

# Let f be solution function.
# Obviously, f(0) = 1, since we can split empty table only into empty set.
# Note that f(2) = 3: (12, 34, 56), (13, 24, 56), (12, 35, 46).
# Also f(n) = 0 if n % 2 == 1 (since total count of pieces is odd).
# Then look at table 3x4. We can split it into two 3x2 pieces (it's f(2)**2 = 9 methods)
# or have two options without it: (14, 23, 58, 69, 7-10, 11-12) and symmetric to it,
# together f(4) = 9 + 2 = 11.
# Let's look at 3xN table. We can split first 3x(2K) (0 <= K <= (n-4)/2) 
# part into one of known parts and parse the remaining such that 
# it doesn't contain 3x2 blocks (two methods). Also we can split into 3x2 and 3x(N-2) blocks;
# that will cover all cases when 3x2 blocks are allowed.
# So f(N) = f(2) * f(N-2) + 2*sum(f(n-4) + ... + f(0))
# Unfortunately, this naive approach doesn't pass last performance test. 
# Simplify the function:
# f(N-2) = f(2) * f(N-4) + 2*sum(f(n-6) + ... + f(0))
# Subtracting this two, we get
# f(N) - f(N-2) = f(2) * (f(N-2) - f(N-4)) + 2*f(N-4)
# We know f(2) = 3, so
# f(N) = 4*f(N-2) - f(N-4)

import sys
sys.setrecursionlimit(100000)

n = int(input())
cache = [None for _ in range(n+1)]
def solve(n):
    if n % 2 == 1: return 0
    if n == 0: return 1
    if n == 2: return 3
    if cache[n] is None:
        cache[n] = 4 * solve(n-2) - solve(n-4)
    return cache[n]

print(solve(n))
