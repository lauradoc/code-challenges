"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

>>> moveZeroes([0,1,0,3,12])
[1,3,12,0,0]
"""

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    
    zero_count = nums.count(0)
    
    for x in range(zero_count):
        nums.remove(0)
        nums.append(0)
    
if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')