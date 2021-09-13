print((lambda s: (lambda x: 'YES' if x%4 == 0 and x%100 != 0 or x%400 == 0 else 'NO')(int(s)))(input()))
