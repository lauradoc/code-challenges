"""
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch
that returns the lowest index i for which arr[i] == i. Return -1 if there is
no such index. Analyze the time and space complexities of your solution and explain its
correctness.
>>> index_equals_value_search([-8,0,2,5])
2
>>> index_equals_value_search([])
-1
>>> index_equals_value_search([-1,0,3,6])
-1
"""


def index_equals_value_search(arr):

    # create a range loop from 0, len(arr)
    # check to see if i == arr[i]
    # if this true i'll return index
    # return -1
    """
    if len(arr) < 1:
      return -1

    for i in range(len(arr)):
      if arr[i] == i:
        return i

    return -1
    """
    # .  0 1 2 3
    # [-8,0,2,5] => 2
    # L = 0, R = 3
    # v = 0, Index = 1
    # if value ? index:
    # how does L or R change

    # [-1,0,3,6]
    # get length of array and divide by two to split array in half
    # check if pivot index = value
    # if value < index then move pivot to smaller half

    # 0 5 6 7

    # Time = O(log(n))
    # Space = O(1)

    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = int((left+right)/2)

        if arr[pivot] == pivot:
            return pivot

        elif arr[pivot] < pivot:
            left = pivot + 1

        else:
            right = pivot - 1

    return -1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
