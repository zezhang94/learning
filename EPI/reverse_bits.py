# Write a program that takes a 64-bit unsigned integer and 
# returns the 64-bit unsigned integer consisting of the bits of the input 
# in reverse order.
def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        return x ^ mask

def reverse_bits(x):
    i = 0
    while i <= 31:
        x = swap_bits(x, i, 63 - i)
        i += 1
    return x

def reverse_bits_lookup_table(x):
    MASK = 0xFFFF
    MASK_SIZE = 16
    PRECOMPUTED_REVERSE = []
    # Reverse all bits, use mask to get 16 bits only.
    return PRECOMPUTED_REVERSE[(x >> (MASK_SIZE * 3)) & MASK]  | \
        PRECOMPUTED_REVERSE[(x >> (MASK_SIZE * 2)) & MASK] << MASK_SIZE | \
        PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & MASK] << (MASK_SIZE * 2) | \
        PRECOMPUTED_REVERSE[x & MASK] << (MASK_SIZE * 3)





 
