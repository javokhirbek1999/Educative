def reverse(testVariable):
  helper(testVariable, 0)
  
def helper(arr, index):
  if index == len(arr) or not arr:
    return []
  
  helper(arr, index+1)
  arr.append(arr[index])
  arr.pop(index)
