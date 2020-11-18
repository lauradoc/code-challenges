"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    s_list = list(s)
    num = ['0','1','2','3','4','5','6','7','8','9']
    result_list = []
    result = ""

    for i in range(len(s_list)):
        if s_list[i].isdigit():
            num = int(s_list[i])
            result_list.append(s_list[i+1+num])

    for letter in result_list:
        result += letter
    
    return result

    #Hackbright's more efficient solution
    # word = ""

    # i = 0

    # while i < len(s):

    #     num_to_skip = int(s[i])
    #     i += num_to_skip + 1

    #     word += s[i]

    #     i += 1

    # return word


if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')