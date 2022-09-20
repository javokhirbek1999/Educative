"""
Time: O(n)
Space: O(1)
"""

def length_of_longest_substring(arr, k):
  
  windowStart = 0
  
  onesCount = 0

  maxLen = 0

  for windowEnd in range(len(arr)):

    left_num = arr[windowEnd]

    if left_num == 1:
      onesCount += 1

    if windowEnd - windowStart + 1 - onesCount > k:
      
      if arr[windowStart] == 1:
        onesCount -= 1
      windowStart += 1
    
    maxLen = max(maxLen, windowEnd - windowStart + 1)
  
  return maxLen
