# Compute the parity of a very large number of 64-bit words

def parity_brute_force(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# tricks
# x & (x - 1) equals x with its lowest set bit erased
def parity_erase_lowest_set_bit(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the lowest set bit of x
    return result