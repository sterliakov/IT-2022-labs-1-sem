STEPS = 2

def walk(x, y, x0, y0, remaining=STEPS):
    if x == x0 and y == y0:
        return remaining
    remaining -= 1
    if remaining == -1 or x <= 0 or y <= 0 or x > 8 or y > 8:
        return -1

    return max(
        walk(x-2, y-1, x0, y0, remaining),
        walk(x-2, y+1, x0, y0, remaining),
        walk(x+2, y-1, x0, y0, remaining),
        walk(x+2, y+1, x0, y0, remaining),
        walk(x-1, y+2, x0, y0, remaining),
        walk(x-1, y-2, x0, y0, remaining),
        walk(x+1, y+2, x0, y0, remaining),
        walk(x+1, y-2, x0, y0, remaining),
    )


ret = walk(int(input()), int(input()), int(input()), int(input()), 2)
print(-1 if ret == -1 else STEPS - ret)
