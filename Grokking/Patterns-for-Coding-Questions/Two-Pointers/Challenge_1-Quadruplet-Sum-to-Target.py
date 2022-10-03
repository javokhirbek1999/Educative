"""
Time: O(n^3)
Space: O(n)
"""

def search_quadruplets(arr, target):
  
  arr.sort()
  n = len(arr)
  
  if n < 4:
    return []
  
  quadruplets = []

  for i in range(n-3):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    for j in range(i+1, n-2):
      if j > i + 1 and arr[j] == arr[j-1]:
        continue

      left = j + 1
      right = n-1

      while left < right:
        
        curr = arr[i] + arr[j] + arr[left] + arr[right]

        if curr == target:
          quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
          left += 1
          right -= 1
        
        if curr < target:
          left += 1
        else:
          right -= 1

  return quadruplets
