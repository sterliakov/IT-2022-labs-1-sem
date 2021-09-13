def det(a):
    if len(a) == 1:
        return a[0][0]
    return sum(map(
        lambda row: a[row][0] * (-1)**row  * det([r[1:] for r in a[:row] + a[row+1:]]), range(len(a))))

print(str(det([list(map(int, input().split())) for _ in range(int(input()))])))
