def find_tribonacci(n):

    # Replace this placeholder return statement with your code
    if n >2:
        t = [0 for i in range(n+1)]
        t[0] = 0
        t[1] = 1
        t[2] = 1
        
        for i in range(3, n+1):
            t[i] = t[i-1] + t[i-2] + t[i-3]

        return t[n]
    else:
        t = [0,1,1]
        return t[n]