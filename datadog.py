"""
    Given array of values, write function that outputs all the prime
    numbers that include 2nd digit of my birthday

>>> output_prime_nums([3, 5, 7, 9, 13, 16, 19, 29, 36, 43, 19, 49], 9)
[19, 29, 19]
"""


def output_prime_nums(nums, birthdate):

    # first check to see if num is prime
    # loop through each num and check to see if it is divisible by a num
    # between 2 and num and check to see if it includes birthday digit
    # if yes, add num to result list

    result = []

    for num in nums:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                if str(birthdate) in str(num):
                    result.append(num)

    return result


"""
    write function that follows this pattern.
    fn(pattern, word) bool
    >>> fn("d1tadog", "datadog")
    True
    >>> fn("d2adog", "datadog")
    True
    >>> fn("d5dog", "datadog")
    False
    >>> fn("d2tadog", "datadog")
    False
    >>> fn("datadog", "datadog")
    True
    >>> fn("2", "ae")
    True
    >>> fn("2eeee", "e")
    False
"""


def fn(pattern, word):

    # loop through each char in pattern
    # if char is numeric
    # take length of word and subtract (num - 1)
    # if lengths match return true
    # else return false

    if pattern == word:
        return True

    for char in pattern:
        if char.isnumeric():
            char_num = int(char)
            return len(pattern) == len(word) - (char_num - 1)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
