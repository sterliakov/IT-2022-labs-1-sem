print(*map(lambda s: sum(ord(el) for el in s), 
           sorted(input().split(), key=lambda s: (len(s), s))))
