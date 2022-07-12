"""
Kaden's Algorithms

Time: O(n)
Space: O(1)
"""
def find_max_sum_sub_array(nums, n):

  if n < 1:
    return 0
  
  global_max, current_max = nums[0], nums[0]

  for current_index in range(1, len(nums)):
    if current_max < 0:
      current_max = nums[current_index]
    else:
      current_max += nums[current_index]
    
    global_max = max(global_max, current_max)
  
  return global_max
