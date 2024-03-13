# Precompute the table
BIT_COUNT = [bin(i).count('1') for i in range(256)]
print(BIT_COUNT)
def count_bits(n):
    return (BIT_COUNT[n & 0xff] +
            BIT_COUNT[(n >> 8) & 0xff] +
            BIT_COUNT[(n >> 16) & 0xff] +
            BIT_COUNT[n >> 24])
    
    
print(count_bits(0b00000000000000000000000000001011))