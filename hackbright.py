"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

>>> mode([1])
{1}

>>> mode([1, 2, 2, 2])
{2}

>>> mode([1, 1, 2, 2])
{1, 2}
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    # loop through each num in nums
    # add num as key to dictionary with 1 as value
    # if num is already in dict increase val by 1

    # find max from vals and add each key to set

    num_count = {}

    for num in nums:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1

    max_count = max(num_count.values())

    mode = set()

    for num, count in num_count.items():
        if count == max_count:
            mode.add(num)

    return mode


"""

Given an integer, print each digit in reverse order, starting with the ones place.

For example, if you were given 1 you should simply print 1, if given 314 you should print 4, 1, 3, and if given 12 you should print 2, 1:

>>> print_digits(1)
1
>>> print_digits(314)
4
1
3
>>> print_digits(12)
2
1
"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while num:
        next_dig = num % 10
        print(next_dig)
        num = (num - next_dig) // 10


"""Split a string by splitter and return list of splits.

This should work like the built-in Python .split() method [*].
YOU MAY NOT USE the .split() method in your solution!
YOU MAY NOT USE regular expressions in your solution!

For example:

    >>> split("i love balloonicorn", " ")
    ['i', 'love', 'balloonicorn']

    >>> split("that is which is that which is that", " that ")
    ['that is which is', 'which is that']

    >>> split("that is which is that which is that", "that")
    ['', ' is which is ', ' which is ', '']

    >>> split("hello world", "nope")
    ['hello world']

* Note: the actual Python split method has special behavior
  when it is not passed anything for the splitter -- you do
  not need to implement that.

"""


def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    # loop over string in sliced increments, where slice is length of splitter
    # if slice matches splitter
    # remove chars before and add to new list

    # i = 0
    # j = len(splitter)
    # result = []

    # while j < len(astring):
    #     print(j, len(astring))
    #     if astring[i:j] == splitter:
    #         result.append(astring[:i])
    #         astring.replace(astring[:i+len(splitter)], "")
    #         i = 0
    #         j = len(splitter)
    #     else:
    #         i += 1
    #         j += 1

    # result.append(astring[:])

    # return result

    out = []
    index = 0

    while index <= len(astring):

        curr_index = index
        index = astring.find(splitter, index)

        if index != -1:
            out.append(astring[curr_index:index])
            index += len(splitter)

        else:
            # couldn't find any more instances of splitter in astring
            out.append(astring[curr_index:])
            break

    return out


"""
Given two already-sorted lists:

Write a function that returns a new list that is the sorted merge of both of them. For the above lists, our result would be:

>>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
[1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    result = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


"""
Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, “racecar”, “tacocat”). An anagram is a rescrambling of a word
(eg for “racecar”, you could rescramble this as “arceace”).

Determine if the given word is a re-scrambling of a palindrome.

The word will only contain lowercase letters, a-z.
>>> is_anagram_of_palindrome("a")
True
>>> is_anagram_of_palindrome("ab")
False
>>> is_anagram_of_palindrome("aab")
True
>>> is_anagram_of_palindrome("arceace")
True
>>> is_anagram_of_palindrome("arceaceb")
False
"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # get length of word
    # loop through each char of word
    # count occurrences of each char with dictionary
    # if length of word is even
    # every character should have even number of counts
    # if length is odd
    # every char should have even counts except one

    length = len(word)
    char_count_dict = {}

    for char in word:
        char_count = word.count(char)
        char_count_dict[char_count] = char

    count = 0

    for key in char_count_dict:
        if length % 2 == 0 and key % 2 != 0:
            return False
        elif length % 2 != 0 and key % 2 != 0:
            count += 1

    if count > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
