"""
Time: O(n)
Space: O(1)
"""


import math


def max_sub_array_of_size_k(k, arr):
  
  windowStart, windowMax = 0, -math.inf

  currentSum = 0

  for windowEnd in range(len(arr)):
    
    currentSum += arr[windowEnd]

    if windowEnd == windowStart + k - 1:
      
      windowMax = max(windowMax, currentSum)

      currentSum -= arr[windowStart]

      windowStart += 1
  
  return windowMax
