# Write a program which takes as input a nonnegative integer x and 
# returns a number y which is not equal to x, but has the same weight as x 
# and their difference, |y - x|, is as small as possible.
#
# Define the 'weight' of a nonnegative integer x to be the number of bits 
# that are set to 1 in its binary representation. 

def swap_bits(x, i, j):
    return x ^ ((1 << i) | (1 << j))

def find_closest_same_weight(x):
    source = x
    count = 0
    while x > 0:
        last = x & 1
        x >>= 1
        if last != x & 1:
            return swap_bits(source, count, count + 1)
        count += 1

# More elegant
def closest_int_same_bit_count(x):
    INT_SIZE = 64
    for i in range(INT_SIZE):
        if (x << i) & 1 != (x << (i + 1)) & 1:
            return x ^ ((1 << i) | (1 << (i + 1)))

# O(1)
def closest_int_same_bit_count_fast(x):
    first = x & ~ (x - 1)
    if first != 1:
        return x - (first >> 1)
    first = x ^ (x + 1)
    return x + (first >> 2) + 1