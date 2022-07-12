"""
N = length of an array
S = Total sum of numbers

Time: O(N*S)

"""
def can_partition(num):
  
  total_sum = sum(num)

  if total_sum % 2 != 0:
    return False
  
  dp = [[-1 for _ in range((total_sum//2)+1)] for _ in range(len(num))]
  
  return True if partition_rec(num, total_sum//2, 0, dp) == 1 else False


def partition_rec(arr, sm, current_index, dp):

  if sm == 0:
    return 1
  
  if len(arr) == 0 or current_index >= len(arr):
    return 0
  
  if dp[current_index][sm] == -1:
    
    if arr[current_index] <= sm:
      if partition_rec(arr, sm-arr[current_index], current_index+1, dp) == 1:
        dp[current_index] = 1
        return 1
  
  dp[current_index][sm] = partition_rec(arr, sm, current_index+1, dp)

  return dp[current_index][sm]
