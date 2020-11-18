"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

>>> numJewelsInStones("aA", "aAAbbbb")
3
>>> numJewelsInStones("z", "ZZ")
0
"""

def numJewelsInStones(J, S):
        
    #loop through S to see if any of the characters match a character in j
    #if there is a match then a counter variable will increase by 1
    
    J_list = J.split()
    counter = 0
    
    for char in S:
        if char in J:
            counter += 1
    
    return counter

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')