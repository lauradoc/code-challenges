import math
import os
import random
import re
import sys

"""
Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers

>>> hourglassSum([[1 1 1 0 0 0],
[0 1 0 0 0 0],
[1 1 1 0 0 0],
[0 0 2 4 4 0],
[0 0 0 2 0 0],
[0 0 1 2 4 0]])
19
"""
# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    # first find sum of first possible hourglass
    # then increase each x index by one until it hits end of row
    # check to see if sum is great than previous sum
    # once end of row is hit then increase y index by one
    # continue until end of list
    # return greatest sumwhile y < 6:

    greatest_sum = arr[0][0]

    while y < 6:
        for x in range(0,6):
            for y in range(1,6):
                while x < 4:
                    hourglass_sum = (arr[x] + arr[x+1] + arr[x+2] + arr[y][x+1] + arr[y+1][x] + arr[y+1][x+1] + arr[y+1][x+2]
                    if hourglass_sum > greatest_sum:
                        greatest_sum = hourglass_sum

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')