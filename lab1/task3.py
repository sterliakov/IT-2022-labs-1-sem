a, b, c = sorted([int(input()) for _ in range(3)])
if c >= a + b:
    print('impossible')
elif c**2 > a**2 + b**2:
    print('obtuse')
elif c**2 == a**2 + b**2:
    print('right')
else:
    print('acute')
