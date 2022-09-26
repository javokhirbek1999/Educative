"""
Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array


Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4

Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9]


Time: O(n)
Space: O(1)
"""



def remove_element(arr, key):
  nextElement = 0  # index of the next element which is not 'key'
  for i in range(len(arr)):
    if arr[i] != key:
      arr[nextElement] = arr[i]
      nextElement += 1

  return nextElement
