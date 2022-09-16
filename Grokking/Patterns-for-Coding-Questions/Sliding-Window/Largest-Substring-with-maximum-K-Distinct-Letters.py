"""
Time: O(N) - outer loop runs only once for each character 
Space: O(K) - K different letters
"""

from collections import defaultdict

def longest_substring_with_k_distinct(str1, k):
  
  windowStart = 0

  vis = defaultdict(int)

  max_len = 0

  for windowEnd in range(len(str1)):

    right_char = str1[windowEnd]

    if right_char not in vis:
      vis[right_char] += 1
    

    while len(vis) > k:
      left_char = str1[windowStart]

      vis[left_char] -= 1

      if vis[left_char] == 0:
        vis.pop(left_char)
      
      windowStart += 1
    
    max_len = max(max_len, windowEnd - windowStart + 1)

  return max_len

