def make_exchange(value, coins, left=0):
    if value < 0:
        return 0
    elif value == 0:
        return 1
    return sum(map(lambda ix: make_exchange(value-ix[1], coins, left+ix[0]), enumerate(coins[left:])))
