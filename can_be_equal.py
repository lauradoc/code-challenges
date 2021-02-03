"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

>>> canBeEqual([1,2,3,4], [2,4,1,3])
True
"""


def canBeEqual(target, arr):

    # check to see if arr contains same values as target
    # if no return false

    #         arr.sort()
    #         target.sort()

    #         for num in arr:
    #             if num not in target:
    #                 return False

    #             if arr == target:
    #                 return True

    return sorted(target) == sorted(arr)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
