def is_add_35(x):
    if x <= 0: return False
    elif x == 1: return True
    return is_add_35(x-3) or is_add_35(x-5)
