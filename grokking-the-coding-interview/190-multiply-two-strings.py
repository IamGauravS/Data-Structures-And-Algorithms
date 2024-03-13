def multiply_strings(str1, str2):
    n1, n2 = len(str1), len(str2)
    result = [0] * (n1 + n2)
    
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            product = (ord(str1[i]) - ord('0')) * (ord(str2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total = product + result[p2]
            
            result[p1] += total // 10
            result[p2] = total % 10
            
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
        
    return ''.join(map(str, result))