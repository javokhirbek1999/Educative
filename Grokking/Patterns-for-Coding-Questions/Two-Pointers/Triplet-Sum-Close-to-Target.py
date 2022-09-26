"""
Time: O(n^2)
Space: O(1)
"""

import math

def triplet_sum_close_to_target(arr, target_sum):
  
  arr.sort()

  closest_sum = math.inf

  for i in range(len(arr)-2):

    left = i+1
    right = len(arr)-1

    while left < right:
      
      target_diff = target_sum - arr[i] - arr[left] - arr[right]

      if target_diff == 0:
        return target_sum
      
      if abs(target_diff) < abs(closest_sum) or (abs(target_diff) == abs(closest_sum) and target_diff > closest_sum):
        closest_sum = target_diff
      
      if target_diff > 0:
        left += 1
      else:
        right -= 1
  print(closest_sum)
  return target_sum - closest_sum

