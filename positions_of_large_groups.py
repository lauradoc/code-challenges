"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

>>> largeGroupPositions("abbxxxxzzy")
[[3, 6]]
>>> largeGroupPositions("abc")
[]
>>> largeGroupPositions("abcdddeeeeaabbbcd")
[[3, 5], [6, 9], [12, 14]]
>>> largeGroupPositions("aba")
[]
"""

def largeGroupPositions(s):
        
#         result = []
    
#         for i, char in enumerate(s[1:]):
#             char_track = s[0]
#             if char == char_track:
#                 char_track = s[i]
#                 if counter > 2:
#             else:
#                 char_track = char
    
    result = []
    counter = 0
    char_track = s[0]
    start = 0
            
    for i in range(len(s)):
        
        if s[i] == char_track:
            counter += 1
            
            if i == len(s)-1 and counter > 2:
                end = i
                result.append([start, end])
            
        elif s[i] != char_track and counter > 2:
            end = i-1
            result.append([start, end])
            start = i
            counter = 1
            char_track = s[i]
            
        else:
            counter = 1
            char_track = s[i]
            start = i
                
                
        # else:
        #     counter = 0
        #     start = i
        #     char_track = s[i]
        
    return result

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')