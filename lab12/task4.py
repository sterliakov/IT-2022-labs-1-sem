def levenshtein(text1, text2):
    l1, l2 = len(text1), len(text2)
    d = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    for t1 in range(l1 + 1):
        d[t1][0] = t1

    for t2 in range(l2 + 1):
        d[0][t2] = t2

    a = b = c = 0

    for t1 in range(1, l1 + 1):
        for t2 in range(1, l2 + 1):
            if (text1[t1-1] == text2[t2-1]):
                d[t1][t2] = d[t1 - 1][t2 - 1]
            else:
                a = d[t1][t2 - 1]
                b = d[t1 - 1][t2]
                c = d[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    d[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    d[t1][t2] = b + 1
                else:
                    d[t1][t2] = c + 1

    return d[-1][-1]

print(levenshtein(input(), input()))
