a = int(input())
b = int(input())

while a and b:
    if a > b:
        a %= b
    else:
        b %= a
print(a or b)
