"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
>>> kidsWithCandies([2,3,5,1,3], 3)
[True, True, True, False, True] 
>>> kidsWithCandies([4,2,1,1,2], 1)
[True, False, False, False, False] 
>>> kidsWithCandies([12,1,12], 10)
[True, False, True]
"""

def kidsWithCandies(candies, extraCandies):
        
    # write a variable that will hold the greatest num of possible candies
    
    # loop through the list of candies using range 
    # check to see if the integer added with the extraCandies int is greater than or equal to the variable above
    # if it is return
    
    max_candies = max(candies)
    result = []
    
    for i in range(len(candies)):
        if candies[i] == max_candies:
            result.append(True)
        elif candies[i] + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    
    return result

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')