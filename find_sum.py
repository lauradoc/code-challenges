"""
triplebyte question

>>> find_sum([1,2,3])
14
"""

def find_sum(nums):
    return sum(x*x for x in nums)

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')