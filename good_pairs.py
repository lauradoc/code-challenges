"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
>>> numIdenticalPairs([1,2,3,1,1,3])
4
>>> numIdenticalPairs([1,1,1,1])
6
>>> numIdenticalPairs([1,2,3,])
0
"""

def numIdenticalPairs(nums):
        
    # loop through the list of nums looking at i 
    # with a nested for loop starting at j, which will be i+1 to start
    # setting a condition if nums[i] == nums[j] then add 1 to the counter
    
    good_pairs = 0
    
    for i in range(len(nums)):
        for j in nums[i+1:]:
            if nums[i] == j:
                good_pairs += 1
                        
    return good_pairs

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')