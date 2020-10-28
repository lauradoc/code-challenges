"""
Given an array nums of integers, return how many of them contain an even number of digits.

>>> findNumbers([12,345,2,6,7896])
2
>>> findNumbers([555,901,482,1771])
1
"""


def findNumbers(nums):
        
        #loop through each number
        #turn num into string and check if length is divisible by 2
        #if it is then add 1 to a counter variable
        #return counter
        
        counter = 0
        
        for num in nums:
            str_num = str(num)
            if len(str_num) % 2 == 0:
                counter += 1
                
        return counter


if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')