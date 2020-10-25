#         sub_sum = sum(nums[:])
#         start = nums[0]
#         end = nums[-1]
        
#         while 
#         for num in nums:
#             slice_sum = sum(nums[num:num+1])
#             if slice_sum > sub_sum:
#                 sub_sum = slice_sum
#                 i += 1
        
#         return sub_sum

#         sub_sum = max(nums)
    
#         if len(nums) < 3:
#             if sum(nums) > sub_sum:
#                 sub_sum = sum(nums)
#             return sub_sum
    
#         for i, num in enumerate(nums):
#             for x in nums[1:]:
#                 slice_sum = sum(nums[i:(x+1)])
#                 print(num, x, (nums[i:(x+1)]))
#                 if slice_sum > sub_sum:
#                     sub_sum = slice_sum
                
#         return sub_sum

#         halfway = int(len(nums)/2)
    
#         left_half = nums[:halfway]
#         left_sum = []
        
#         for num in left_half:
#             new_sum = sum(num)
        
        
#         right_half = nums[halfway:]
#         right_sum = []



        max_so_far = nums[0]
        elements_so_far = [nums[0]]
        
        for num in nums[1:]:
            if num > sum(elements_so_far + [num]):
                elements_so_far = [num]
            else:
                elements_so_far.append(num)
                
            max_so_far = max(max_so_far, sum(elements_so_far))
            
        return max_so_far
    