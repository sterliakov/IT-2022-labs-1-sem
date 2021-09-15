def prefix(s):
    pi = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]: 
            j = pi[j-1]
        if s[i] == s[j]: j += 1
        pi[i] = j
    return pi


def search(s, p):
    pi = prefix(p + '@' + s)
    return [i - 2*len(p) for i, el in enumerate(pi) if el == len(p)] or [-1]

s = input()
p = input()
print(search(s*2, p)[0])
