from math import floor


LENGTHS = {
    'monkey': 90,
    'parrot': 10,
    'elephant': 300,
}

print(max(1, floor(int(input()) / LENGTHS[input()])))
