"""
Given two strings s and t , write a function to determine if t is an anagram of s.
>>> isAnagram("anagram", "nagaram")
True
>>> isAnagram("car", "rat")
False
"""

def isAnagram(s, t):
                
    if len(s) == len(t):
        if len(s) == 0:
            return True
        elif sorted(s) == sorted(t):
            return True
        else:
            return False

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')