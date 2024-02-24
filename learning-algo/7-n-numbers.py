def calculate_sum(n):
    if n == 0:
        return 0 
    return n +  calculate_sum(n-1)


print(calculate_sum(5))

def reverse_array_helper(arr, n, new_arr):
    if len(arr) == n:
        return
    reverse_array_helper(arr, n+1, new_arr)
    new_arr.append(arr[n])



def reverse_array(arr):
    new_arr = []
    reverse_array_helper(arr, 0, new_arr)
    return new_arr

print(reverse_array([1,2,3,4,11]))

def check_if_pallindrom_helper(input_str, n):
    if n > len(input_str)//2:
        return True 
    if input_str[n] != input_str[len(input_str)-1-n]:
        return False 
    return check_if_pallindrom_helper(input_str, n+1)

def check_if_pallindrom(input_str):
    if len(input_str) == 1:
        return True 
    
    return check_if_pallindrom_helper(input_str, 0)

print(check_if_pallindrom('abcbad'))

def calculate_fibinaci_number(n):
    if n == 0:
        return 0 
    if n==1:
        return 1
    return calculate_fibinaci_number(n-1) + calculate_fibinaci_number(n-2)

print(calculate_fibinaci_number(6))