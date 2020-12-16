"""
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.

Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

>>> get_different_number([0, 1, 2, 3])
4
>>> get_different_number([0])
1
>>> get_different_number([0, 1, 2])
3
>>> get_different_number([1,3,0,2])
4
>>> get_different_number([100000])
0
>>> get_different_number([1,0,3,4,5])
2
>>> get_different_number([0,100000])
1
>>> get_different_number([0,99999,100000])
1
>>> get_different_number([0,5,4,1,3,6,2])
7
"""

def get_different_number(arr):

  possible_mins = []
  result = []
  lowest_val = min(arr)
  
  if lowest_val > 0:
    return 0
  
  for num in arr:
    possible_mins.append(num + 1)

  for x in possible_mins:
    if x not in arr:
      result.append(x)
  
  return min(result)

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')