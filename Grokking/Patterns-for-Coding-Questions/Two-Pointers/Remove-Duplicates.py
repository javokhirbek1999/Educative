"""
Time: O(n)
Space: O(1)
"""

def remove_duplicates(arr):
  
  first, second = 0, 0

  count = 0

  while second != len(arr):

    if arr[second] == arr[first]:
      second += 1
    else:
      first += 1
      count += 1

  return count-1

