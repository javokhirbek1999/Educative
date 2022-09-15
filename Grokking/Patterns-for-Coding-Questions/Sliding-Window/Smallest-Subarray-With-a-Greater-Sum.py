"""
Time: O(n)
Space: O(1)
"""

import math

def smallest_subarray_sum(s, arr):
  
  windowStart, windowSum = 0, 0

  min_len = math.inf

  for windowEnd in range(len(arr)):

    windowSum += arr[windowEnd]

    while windowSum >= s:
      min_len = min(min_len, windowEnd - windowStart + 1)

      windowSum -= arr[windowStart]

      windowStart += 1
  

  return 0 if min_len == math.inf else min_len

