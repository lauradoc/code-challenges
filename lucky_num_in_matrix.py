"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
>>> luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
[15]
>>> luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
[12]
>>> luckyNumbers([[7,8],[1,2]])
[7]
"""

def luckyNumbers (matrix):
        
        luckyNums = []
        smallest = []
        i = 0
        
        for row in matrix:
            smallest.append(min(row))
            
        while i < len(matrix[0]):
            column = [row[i] for row in matrix]
            if max(column) in smallest:
                luckyNums.append(max(column))
            i += 1
            
        return luckyNums

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')