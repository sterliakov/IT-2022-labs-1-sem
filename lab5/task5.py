input()
s0 = input().replace(' ', '')
s = s0 + s0[::-1]

def is_pal(s):
    for c1, c2 in zip(s, s[::-1]):
        if c1 != c2:
            return False
    return True

l = len(s0)
for i in range(l, 2*l + 1):
    if is_pal(s[:l] + s[i:]):
        M = 2*l - i

print(M)
print(*list(s0[:M][::-1]))
