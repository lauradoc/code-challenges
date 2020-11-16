# """
# Given an integer n and an array a of length n, your task is to apply the following mutation to a:

#     Array a mutates into a new array b of length n.
#     For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
#     If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. 
#     For example, b[0] should be equal to 0 + a[0] + a[1].
# >>> mutateArray(5, [4, 0, 1, -2, 3])
# [4, 5, -1, 2, 1]
# """

# def mutateArray(n, a):

#     array_b = []

#     for i in range(n):
#         if i == 0:
#             new_num = 0 + a[i] + a[i+1]
#             array_b.append(new_num)

#         elif i >= n-1:
#             new_num = a[i-1] + a[i] + 0
#             array_b.append(new_num)
        
#         else:
#             new_num = a[i-1] + a[i] + a[i+1]
#             array_b.append(new_num)

#     return array_b


# """
# You are given two arrays of integers a and b of the same length, and an integer k. We will be 
# iterating through array a from left to right, and simultaneously through array b from right to 
# left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny 
# if the concatenation xy is strictly less than k.

# Your task is to return the number of tiny pairs that you'll encounter during the simultaneous 
# iteration through a and b.
# >>> countTinyPairs([1, 2, 3], [1, 2, 3], 31):
# 2
# >>> countTinyPairs([16, 1, 4, 2, 14], [7, 11, 2, 0, 15], 743)
# 4
# """

# def countTinyPairs(a, b, k):

#     tiny_pairs = 0

#     for x in range(len(a)):
#         for y in range(len(b[::-1])):
#             concat = str(a[x]) + str(b[y])
#             if int(concat) < k:
#                 tiny_pairs += 1

#     return tiny_pairs


"""
You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, 
so that arrays with equal mean values are in the same group, and arrays with different mean values
are in different groups.

Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i],
a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the 
indices within each group are sorted in ascending order, and the groups are sorted in ascending 
order of their minimum element.
>>> meanGroups([[3, 3, 4, 2], [4, 4], [4, 0, 3, 3], [2, 3], [3, 3, 3]])
[[0, 4], [1], [2, 3]]
>>> meanGroups([[-5, 2, 3], [0, 0], [0], [-100, 100]])
[[0, 1, 2, 3]]
"""

def meanGroups(a):

    result = []
    mean_index_dict = {}

    for i in range(len(a)):
        mean = (sum(a[i])/len(a[i]))
        if mean not in mean_index_dict:
            mean_index_dict[mean] = [i]
        else:
            mean_index_dict[mean].append(i)

    for key, value in mean_index_dict.items():
        result.append(value)
    return result
        

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')