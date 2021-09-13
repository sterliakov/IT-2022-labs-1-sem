def bitwise_sort(arr):
    md = 1
    flag = True
    while flag:
        flag = False
        buf0 = []
        buf1 = []
        for el in arr:
            s = el // md
            if s > 0:
                if s % 2 == 0:
                    buf0.append(el)
                else:
                    buf1.append(el)
                flag = True
            else:
                buf0.append(el)
        del arr
        arr = buf0 + buf1
        del buf0; del buf1
        md *= 2
        if flag:
            print(*map(lambda x: bin(x)[2:], arr))

bitwise_sort(list(map(lambda x: int(x,2), input().split())))
