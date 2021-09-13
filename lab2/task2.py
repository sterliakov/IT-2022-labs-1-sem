print((lambda s: (lambda x: x%10 + x%100//10 + x//100)(int(s)))(input()))
