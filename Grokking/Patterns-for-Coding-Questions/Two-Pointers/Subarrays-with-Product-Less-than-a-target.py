"""
Time: O(n^2)
Space: O(n^3)
"""

from collections import deque

def find_subarrays(arr, target):
  result = []
  
  n = len(arr)
  
  product = 1

  left = 0

  for right in range(n):

    product *= arr[right]

    while left <= right and product >= target:

      product /= arr[left]

      left += 1

    temp = deque()

    for i in range(right, left-1, -1):
      temp.appendleft(arr[i])
      result.append(list(temp))


  return result
