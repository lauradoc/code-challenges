# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def twoSum(nums, target):
    """
    >>> twoSum([2,7,11,15], 9)
    [0,1]
    >>> twoSum([3,2,4], 6)
    [1,2]
    >>> twoSum([3,3], 6)
    [0,1]
    """
        
    index_num_dict = {}
    
    for i, num in enumerate(nums):
        x = target - num
        if x not in index_num_dict:
            index_num_dict[num] = i
        else:
            return [index_num_dict[x], i]

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')