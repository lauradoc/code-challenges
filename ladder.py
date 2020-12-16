# Implement a function that converts a non-negative integer to a string.
# 
# Examples:
# 
# itoa(12345) => "12345"
# itoa(0) => "0"
# 
# 
# 12345 % 10 = 5
# 12345 / 10 = 1234

def convert_to_str(num):
    
    #create an empty list
    #while len of the num > 0
    #pop the end number and add to the empty list
    #iterate through list and convert each num to str and concat 
    
    list_of_nums = []
    result = ''
    
    if num == 0:
        return str(num)
    
    if num < 0:
        num = -(num)
        result += '-'
    
    while num > 0:
        
        x = num % 10
        n = num // 10
        num = n
        list_of_nums.append(x)
        # print(list_of_nums)
    
    
    for x in reversed(list_of_nums):
        y = str(x)
        result += y
        
    return result