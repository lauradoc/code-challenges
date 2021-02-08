"""
Write a function that takes an array of numbers (integers for the tests)
and a target number. It should find two different items in the array that,
when added together, give the target value. The indices of these items
should then be returned in a tuple like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any
valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or
greater, and all of the items will be numbers; target will always be the
sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

>>> two_sum([1, 2, 3], 4)
(0, 2)
"""


def two_sum(numbers, target):

    checked = {}

    for i, num in enumerate(numbers):
        check_num = target - num
        if check_num in checked:
            return (checked.get(check_num), i)
        checked[num] = i


"""
Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

>>> explode("312")
"333122"
>>> explode("102269")
"12222666666999999999"
"""


def explode(s):

    # first loop through each character and turn character into int
    # add that character to a string variable int number of times
    # return that string

    result = ""

    for char in s:
        num_char = int(char)
        i = 1
        while i <= num_char:

            result += char
            i += 1

    return result


"""
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
>>> remove_smallest([1,2,3,4,5])
[2,3,4,5]
>>> remove_smallest([5,3,2,1,4])
[5,3,2,4]
>>> remove_smallest([2,2,1,2,1])
[2,2,2,1]
"""


def remove_smallest(numbers):

    if numbers == []:
        return numbers

    a = numbers[:]
    a.remove(min(a))
    return a


"""
Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).

Note
If num is negative, ignore its sign and treat it as a positive value
If nth is not positive, return -1
Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
>>> findDigit(5673, 4)
5
>>> findDigit(129, 2)
2
>>> findDigit(-2825, 3)
8
>>> findDigit(-456, 4)
0
>>> findDigit(0, 20)
0
>>> findDigit(65, 0)
-1
>>> findDigit(24, -8)
-1
"""


def findDigit(num, nth):

    # if nth <= 0 return -1
    # index variable equals length of num(as a str) -  nth
    # if index variable is less than 0
    # return 0
    # iterate through num (str)
    # return the value at the index (int)

    if nth <= 0:
        return -1
    if num < 0:
        num = -num

    index = len(str(num)) - nth

    if index < 0:
        return 0

    else:
        str_result = str(num)[index]
        return int(str_result)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
