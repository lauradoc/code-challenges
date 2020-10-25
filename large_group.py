
def largeGroupPositions(s):
    """
    >>> largeGroupPositions("abbxxxxzzy")
    [[3, 6]]

    >>> largeGroupPositions("aba")
    []
    """

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
        
    return result

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')