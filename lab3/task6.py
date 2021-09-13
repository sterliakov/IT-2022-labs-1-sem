import time
import re
import string

def naive(s):
    curr = ''
    mx = None
    for c in s + '@':
        if c in string.digits:
            curr = curr + c
        elif curr:
            x = int(curr)
            if mx is None or mx < x:
                mx = x
            curr = ''
    return mx or 0

def regex(s):
    return max(map(int, re.findall(r'\d+', s) or '0'))

print(regex(input()))
