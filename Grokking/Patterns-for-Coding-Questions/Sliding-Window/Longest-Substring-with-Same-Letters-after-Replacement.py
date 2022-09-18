"""
Time: O(n)
Space: O(1)
"""

def length_of_longest_substring(str1, k):
  
  windowStart = 0

  max_len = 0
  
  vis = {}
  temp = k

  max_repeat_count = 0

  for windowEnd in range(len(str1)):

    left_char = str1[windowEnd]

    if left_char not in vis:
      vis[left_char] = 0  
    vis[left_char] += 1

    max_repeat_count = max(max_repeat_count, vis[left_char])

    if windowEnd - windowStart + 1 - max_repeat_count > k:

      right_char = str1[windowStart]

      vis[right_char] -= 1

      windowStart += 1
    
    max_len = max(max_len, windowEnd - windowStart + 1)
  
  return max_len
