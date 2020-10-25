"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

>>> singleNumber([2,2,1])
1
>>> singleNumber([4,1,2,1,2])
4
>>> singleNumber([1])
1
"""

def singleNumber(nums):
        
    # loop through the list and append each number to an empty list that i'll use to check to see if the number is already in the list
    
    counter_dict = {}
    
    for num in nums:
        if num in counter_dict:
            counter_dict[num] += 1
        else:
            counter_dict[num] = 1
    
    for num in counter_dict:
        if counter_dict[num] == 1:
            return num

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')