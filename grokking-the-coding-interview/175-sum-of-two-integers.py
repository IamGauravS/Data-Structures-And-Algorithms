def integer_addition(a, b):
    # Replace this placeholder return statement with your code
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b 
        b = carry
        
    return a
