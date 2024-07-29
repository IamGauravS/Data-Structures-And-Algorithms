

def find_next_grater_element(nums):
    output = [-1]
    stack = [nums[len(nums)-1]]
    for i in range(len(nums)-2, -1,-1):
        if nums[i] < stack[-1]:
            output.append(stack[-1])
            
        else:
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if stack:
                output.append(stack[-1])
                
            else:
                output.append(-1)
                
        stack.append(nums[i])
                
                
    return output[::-1]
            
            
            


def find_next_grater_element_circular(nums):
    nums = nums+nums
    output = [-1]
    stack = [nums[len(nums)-1]]
    for i in range(len(nums)-2, -1,-1):
        if nums[i] < stack[-1]:
            output.append(stack[-1])
            
        else:
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if stack:
                output.append(stack[-1])
                
            else:
                output.append(-1)
                
        stack.append(nums[i])
                
    output = output[:len(nums)//2]
    return output[::-1]
            
            
def find_next_grater_element_circular(nums):
    n = len(nums)
    output = [-1] * n
    stack = []

    for i in range(2*n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i % n]:
            stack.pop()
        if stack:
            output[i % n] = nums[stack[-1]]
        stack.append(i % n)

    return output