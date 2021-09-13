from datetime import datetime as dt

arr = [dt.strptime(input(), '%d %B %Y %H:%M') for _ in range(int(input()))]
print(*map(lambda x: x.strftime('%-d %B %Y %-H:%M'), sorted(arr)), sep='\n')
