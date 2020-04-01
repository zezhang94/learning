# Implement code that takes as input a 64-bit integer and 
# swaps the bits at indices i and j.
def swap_bits(x, i, j):
    bit_arr = []
    loop = 0
    while loop != 64:
        bit_arr.append(x % 2)
        x = x / 2
        loop += 1
    if bit_arr[i] != bit_arr[j]:
        bit_arr[i], bit_arr[j] = bit_arr[j], bit_arr[i]
    loop -= 1
    while loop >= 0:
        x = x * 2 + bit_arr[loop]
        loop -= 1
    return x

def swap_bit_elegant(x, i, j):
    # Extract the i-th and j-th bits, and see if they differ
    if (x >> i) & 1 != (x >> j) & 1:
        # i-th and j-th bits differ. We will swap then by flipping their values
        # Select the bits to flip with bit_nask. Since x ^ 1 = 0 when x = 1 
        # and 1 when x = 0, we can perforn the flip X1R.
        mask = (1 << i) | (1 << j)
        return x ^ mask
