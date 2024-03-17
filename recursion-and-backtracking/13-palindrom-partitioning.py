def check_if_palindrom(string):
    if len(string) == 0:
        return True
    start = 0
    end = len(string)-1
    
    while start <= end:
        if string[start] != string[end]:
            return False
        start +=1
        end -= 1
    return True

def  palindrom_partition_helper(string, start, end,  output):
    if start >= end:
        return 

    for partition in range(start+1, end+1):
        substring = string[start:partition]
        if check_if_palindrom(substring):
            output.append(substring)
        palindrom_partition_helper(string, partition, end, output)

def get_all_palindrom_substring(string):
    start = 0
    end = len(string)
    output = []
    palindrom_partition_helper(string, start, end, output)
    return output