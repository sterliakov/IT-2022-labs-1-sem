class Point:
    kind = ''
    visited = False

    def __init__(self, kind):
        self.kind = kind


class Solution:
    def __init__(self, w, h, lab):
        self.w = w
        self.h = h
        self.lab = lab

    def walk(self, y, x):
        if self.lab[y][x].visited or self.lab[y][x].kind == '#':
            return False
        if y == 0 or x == 0 or y == self.h - 1 or x == self.w - 1:
            return True
        self.lab[y][x].visited = True

        if y > 0:
            if self.walk(y-1, x):
                return True

        if x > 0:
            if self.walk(y, x-1):
                return True

        if y < self.h - 1:
            if self.walk(y+1, x):
                return True

        if x < self.w - 1:
            if self.walk(y, x+1):
                return True

        return False

    def find_pos(self):
        for i, row in enumerate(self.lab):
            for j, el in enumerate(row):
                if el.kind == '@':
                    return (i, j)

    def __call__(self):
        return self.walk(*self.find_pos())


h, w = map(int, input().split())
lab = [[Point(c) for c in list(input())] for _ in range(h)]
print("YES" if Solution(w, h, lab)() else "NO")
