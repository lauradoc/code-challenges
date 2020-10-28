"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

>>> toLowerCase("Hello")
'hello'
>>> toLowerCase("here")
'here'
>>> toLowerCase("LOVELY")
'lovely'
"""

def toLowerCase(str):
        
        #create an empty list
        #loop through each character
        #check to see if character is uppercase
        #if it is upper then turn to lower and append to list
        #if not upper then append to list
        #use join to turn list into a string
        
        characters = []
        lower_string = ""
        
        for char in str:
            if char <= 'Z' and char >= 'A':
                characters.append(char.lower())
            else:
                characters.append(char)
        
        return lower_string.join(characters)


if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')