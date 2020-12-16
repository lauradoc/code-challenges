"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

>>> interpret("G()(al)")
'Goal'
>>> interpret("G()()()()(al)")
'Gooooal'
>>> interpret("(al)G(al)()()G")
'alGalooG'
"""

def interpret(command):
        
    #create dictionary with key as command and value as string interpretation
    # loop through command and if char is in dictionary then add it's value to an empty string variable
    
    result = ''
    
    command_dict = {'G':'G', '()':'o', '(al)':'al'}
    
    for i in range(len(command)):
        
        if command[i] == 'G':
            result += command_dict['G']
        
        if command[i] == '(' and command[i+1] == ')':
            result += command_dict['()']
            i += 1
        
        if command[i] == '(' and command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
            result += command_dict['(al)']
            i += 3
    
    return result

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')