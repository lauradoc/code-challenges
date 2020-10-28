"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

>>> isValid("()")
True
>>> isValid("()[]{}")
True
>>> isValid("(]")
False
>>> isValid("([)]")
False
>>> isValid("{[]}")
True
"""


def isValid(s):
        
    stack = []
    
    char_dict = {')':'(', '}':'{', ']':'['}
    
    if len(s) % 2 != 0:
        return False
    
    else:
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            elif len(stack) > 0:
                if char_dict[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        if len(stack) == 0:
            return True

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')