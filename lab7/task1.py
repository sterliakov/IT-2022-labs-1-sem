def matryoshka(n):
    if n == 1:
        print('matryoshechka')
        return
    print('verh matryoshki %d' % n)
    matryoshka(n-1)
    print('niz matryoshki %d' % n)
