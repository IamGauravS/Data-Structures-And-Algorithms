

def house_robber(arr):
    dp1 = [0 for i in range(len(arr)-1)]
    
    dp1[0] = arr[0]
    dp1[1] = arr[1]
    for i in range(2, len(arr)-1):
        dp1[i] = max(dp1[i-1], arr[i]+dp1[i-1])
        
    
    
    dp2 = [0 for i in range(len(arr)-1)]
    dp2[0] = arr[1]
    dp2[1] = arr[2]
    
    for i in range(3, len(arr)):
        dp2[i-1] = max(dp2[i-2], arr[i]+dp2[i-3])
        
    return max(dp1[-1], dp2[-1])
    