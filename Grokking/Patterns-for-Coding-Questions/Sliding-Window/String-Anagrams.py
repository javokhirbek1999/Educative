"""
Time: O(n + m)
Space: O(m)
"""

from collections import Counter, deque

def find_string_anagrams(str1, pattern):
  result_indexes = deque()

  c = Counter(pattern)

  windowStart = 0

  vis = {}
  
  for windowEnd in range(len(str1)):

    right_char = str1[windowEnd]

    if right_char not in vis:
      vis[right_char] = 0
    
    vis[right_char] += 1

    result_indexes.append(windowEnd)

    if windowEnd - windowStart + 1 == len(pattern):

      if vis == c:
        return list(result_indexes)
        
      left_char = str1[windowStart]

      vis[left_char] -= 1

      if vis[left_char] == 0:
        vis.pop(left_char)
      
      result_indexes.popleft()

      windowStart += 1
  
  return []

