"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
>>> sortedSquares([-4,-1,0,3,10])
[0, 1, 9, 16, 100]
>>> sortedSquares([-7,-3,2,3,11])
[4, 9, 9, 49, 121]
"""

def sortedSquares(A):
        
    squared_A = []
    
    for num in A:
        squared_A.append(num*num)
        
    return sorted(squared_A[::-1])

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')