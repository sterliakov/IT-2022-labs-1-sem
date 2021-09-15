from collections import Counter

print((lambda counter: (''.join(k * v for k, v in counter)
                        if counter[0][0] != '0'
                        else (counter[1][0]
                              + '0' * counter[0][1]
                              + ''.join(k * (v if k != counter[1][0] else v - 1)
                                        for k, v in counter
                                        if k != '0')
                              )
                        ))
      (sorted(Counter(input()).items())))
