"""
Time: O(n)
Space: O(n)
"""
def find_max_sum_subsequence(nums):

  mx = max(nums)

  if mx < 0:
    return mx

  res = [0] * len(nums)

  for current_index in range(len(nums)):

    if current_index == 0:
      res[0] = nums[0]
    elif current_index == 1:
      res[1] = max(res[0], nums[1])
    else:
      previous_iteration_sum = res[current_index-1]
      previous_second_iteration_sum = res[current_index-2] + nums[current_index]

      res[current_index] = max(previous_iteration_sum, previous_second_iteration_sum)
  
  return res[-1]
