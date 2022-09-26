"""
Time: O(n^2)
Space: O(n)
"""

def search_triplets(arr):
  triplets = []
  
  arr.sort()

  for i in range(len(arr)):

    if i > 0 and arr[i] == arr[i-1]:
      continue
    
    search_triplet(arr, triplets, -arr[i], i+1)

  return triplets


def search_triplet(arr, triplets, target, left):

  right = len(arr)-1

  while left < right:

    current = arr[left] + arr[right]

    if current == target:
      triplets.append([-target, arr[left], arr[right]])

      left += 1
      right -=1 

      while left < right and arr[left] == arr[left-1]:
        left += 1
      while left < right and arr[right] == arr[right+1]:
        right -= 1
    elif current < target:
      left += 1
    else:
      right -= 1
