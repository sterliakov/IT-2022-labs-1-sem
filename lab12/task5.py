def read_lcs(d, s1, s2, x, y):
    if x == 0 or y == 0:
        return []
    if s1[x-1] == s2[y-1]:
        return read_lcs(d, s1, s2, x-1, y-1) + [s1[x-1]]
    if d[y-1][x] > d[y][x-1]:
        return read_lcs(d, s1, s2, x, y-1)
    return read_lcs(d, s1, s2, x-1, y)

def lcs(s1, s2):
    l1, l2 = len(s1), len(s2)
    d = [[0 for _ in range(l1+1)] for _ in range(l2+1)]
    for y in range(1, l2+1):
        for x in range(1, l1+1):
            if s1[x-1] == s2[y-1]:
                d[y][x] = d[y-1][x-1] + 1
            else:
                d[y][x] = max(d[y-1][x], d[y][x-1])

    return read_lcs(d, s1, s2, l1, l2)

# if __name__ == '__main__':
#     print(lcs([1, 5, 7, 8, 9, 2, 4, 6], [3, 6, 7, 5, 7, 6, 1, 2]))
