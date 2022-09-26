"""
Time: O(n^2)
Space: O(1)
"""

def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  n = len(arr)
  
  for i in range(n-2):

    left = i + 1
    right = n - 1

    leftover = target - arr[i]

    while left < right:

      curr = arr[left] + arr[right]

      if curr < leftover:
        count += right - left
        left += 1
      else:
        right -= 1

  return count
