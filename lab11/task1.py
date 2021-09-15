print(*[sum(map(ord, s))
        for s in input().split()
        if len(s) >= 5])
