"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

>>> defangIPaddr("1.1.1.1")
'1[.]1[.]1[.]1'
>>> defangIPaddr("255.100.50.0")
'255[.]100[.]50[.]0'
"""

def defangIPaddr(address):
        
    # loop through the list and check to see if a character is .
    # if it is then replace . with [.]
    
    new_ip = ''
    
    for char in address:
        if char == '.':
            new_ip += "[.]"
        else:
            new_ip += char
        
    return new_ip

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')