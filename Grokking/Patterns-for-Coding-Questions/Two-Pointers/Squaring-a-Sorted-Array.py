"""
Time: O(n)
Space: O(n)
"""


def make_squares(arr):
  
  n = len(arr)

  start, end = 0, n-1

  index = n-1
  
  squares = [0 for _ in range(n)]
  
  while start <= end:

    left = arr[start] * arr[start]
    right = arr[end] * arr[end]

    if left > right:
      squares[index] = left
      start += 1
    else:
      squares[index] = right
      end -= 1
    index -=1 

  return squares
