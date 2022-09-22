"""
n = len(s1)
m = len(s2)

Time: O(n + m)
Space: O(m)
"""

from collections import Counter

def find_permutation(str1, pattern):
  
  windowStart = 0

  c = Counter(pattern)

  vis = {}

  for windowEnd in range(len(str1)):

    right_char = str1[windowEnd]

    if right_char not in vis:
      vis[right_char] = 0
    vis[right_char] += 1

    if windowEnd - windowStart + 1 == len(pattern):
      
      if vis == c:
        return True
      
      left_char = str1[windowStart]

      vis[left_char] -= 1

      if vis[left_char] == 0:
        vis.pop(left_char)
      
      windowStart += 1
  
  return False

  
