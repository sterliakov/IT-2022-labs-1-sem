n = int(input())

ret = ''
while n:
    r = n % 60
    ret = '<' * (r // 10) + 'v' * (r % 10) + '.' + ret
    n //= 60
print(ret[:-1])
