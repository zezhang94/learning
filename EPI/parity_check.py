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

# use lookup table
# TODO calculate PRECOMPUTED_PARITY
def parity_lookup_table(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

# The XOR of a group of bits is its parity.
# 11010111 >> 4
# 00001101 
# 11011010 >> 2
# 00110110
# 11101100 >> 1
# 01110110
# 10011010 extract last bit 
# 00000001
def parity_properties(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

# Right propagate the rightmost set bit in x, e.g., turns (01010000) to (01011111)
def exercise1(x):
    # x & ~ (x - 1) 
    # isolates the lowest bit that is 1 in x; 
    # extracts the lowest set bit of x
    print(bin(~ (~ (x & ~ (x - 1)) + 1) | x))
    # simpler
    print(bin(x | (x - 1)))

# Compute x mod a power of two, e.g., returns 13 for 77 mod 64
def exercise2(x, power):
    print((x ^ power) & (power - 1))
    # simpler
    print(x & (power - 1))
    
# Test if x is a power of 2
def exercise3(x):
    print((x << 1) - 1 == x ^ (x - 1))
    # simpler
    print(x & (x - 1) == 0) 
    

