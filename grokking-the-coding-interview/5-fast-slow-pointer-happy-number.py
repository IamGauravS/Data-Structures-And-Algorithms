def get_squared_of_digit(n):
    digits = [int(digit) for digit in str(n)]
    sum = 0
    for digit in digits:
        sum += (digit**2)
    return sum

def is_happy_number(n):

    # Replace this placeholder return statement with your code
    slow = n 
    fast = get_squared_of_digit(n)
    if fast == 1:
        return True
    while fast != slow:
        if fast == 1:
            return True 
        fast = get_squared_of_digit(get_squared_of_digit(fast))
        slow = get_squared_of_digit(slow)
    
    return False

