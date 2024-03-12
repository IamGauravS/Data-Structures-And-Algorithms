from math import log2, floor

def find_bitwise_complement(num):
    if num == 0:
        return 1
    bit_count = floor(log2(num)) + 1
    all_bit_set = pow(2, bit_count) - 1
    return num ^ all_bit_set