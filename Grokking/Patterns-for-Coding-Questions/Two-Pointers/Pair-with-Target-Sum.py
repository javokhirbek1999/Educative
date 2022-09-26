"""
Time: O(n)
Space: O(1)
"""

def pair_with_targetsum(arr, target_sum):
  
  start, end = 0, len(arr)-1

  while start < end:

    currentSum = arr[start] + arr[end]

    if currentSum == target_sum:
      return [start, end]
    
    if currentSum < target_sum:
      start += 1
    else:
      end -= 1

  return [-1, -1]
