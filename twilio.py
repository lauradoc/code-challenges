    #assessment solutions. Not correct! Only passed one test case each

    #loop through codes to get each character and create a dictionary of all possible number combos
    #check to see if any of the values are in numbers

#given a list of codes and a list of numbers, using t9 translation of the numbers to letters
# return the numbers that contain the code within the number
#ex ABC --> 222, LIST OF NUMS [651724934, 09345872345, 98722244, ]

def vanity(codes, numbers):
    vanity_dict = {'A': [0,1,2], 'B': [0,1,2], 'C': [0,1,2], 'D': [0,1,3], 'E': [0,1,3], 'F': [0,1,3], 'G': [0,1,4], 'H': [0,1,4], 'I': [0,1,4], 'J': [0,1,5], 'K': [0,1,5], 'L': [0,1,5], 'M': [0,1,6], 'N': [0,1,6], 'O': [0,1,6], 'P': [0,1,7], 'Q': [0,1,7], 'R': [0,1,7], 'S': [0,1,7], 'T': [0,1,8], 'U': [0,1,8], 'V': [0,1,8], 'W':[0,1,9], 'X':[0,1,9], 'Y':[0,1,9], 'Z':[0,1,9]}
    
    number_options = []
    
    result = []
    for code in codes:
        for char in codes:
            number_options.append(vanity_dict[char])
    
    print(number_options)
    
    for i in range(len(numbers)):
        if numbers[i] in number_options[i]:
            result.append(numbers[i])
    
    return result



    # The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

def segments(message):
    #get the length of the message and divide by 160
    #iterate through message and break at 160. Append this break into a new list of strings.
    
    results = []
    
    n = round(len(message)/160)
    i = 1
    
    while message:
        results.append(message[:160])
        if n > 1:
            results.append(f'({i}/{n})')
        message = message[160:]
        i += 1
        
    return results
