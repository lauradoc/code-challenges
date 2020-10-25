"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

>>> removeDuplicates([1,1,2])
2
>>> removeDuplicates([0,0,1,1,1,2,2,3,3,4])
5
"""


def removeDuplicates(nums):
        
    for i in reversed(range(1, len(nums))):
        if nums[i] == nums[i-1]:
            nums.pop(i)

    return len(nums)


if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')