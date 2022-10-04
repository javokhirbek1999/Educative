"""
Time: O(n)
Space: O(1)
"""

def shortest_window_sort(arr):

  low = 0
  high = len(arr)-1

  while low < len(arr)-1 and arr[low] <= arr[low+1]:
    low += 1
  
  if low == len(arr)-1:
    return 0
  
  while high > 0 and arr[high] >= arr[high-1]:
    high -= 1
  

  subMax = -float('inf')
  subMin = float('inf')

  for k in range(low, high+1):
    subMax = max(subMax, arr[k])
    subMin = min(subMin, arr[k])
  
  
  while low > 0 and arr[low-1] > subMin:
    low -= 1
  
  while high < len(arr)-1 and arr[high+1] < subMax:
    high += 1
  
  return high - low + 1
