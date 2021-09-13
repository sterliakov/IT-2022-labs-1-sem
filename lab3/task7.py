MAX_SPEED = 60
END_NUMBER = 'A999AA'

def price(s):
    x = len(set(s[1:4]))
    if x == 1: return 1000
    elif x ==2: return 500
    else: return 100

total = 0
while True:
    v, s = input().split()
    if s == END_NUMBER:
        break
    if int(v) > MAX_SPEED:
        total += price(s)
print(total)
