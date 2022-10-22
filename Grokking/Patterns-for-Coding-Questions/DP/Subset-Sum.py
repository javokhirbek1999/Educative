"""
Time: O(n * m)
Space: O(n * m)
"""
def can_partition(num, sum):

  dp = [[-1 for _ in range(sum + 1)] for _ in range(len(num) + 1)]

  return canPartition(num, sum, 0, dp) == 1

def canPartition(num, sm, current_index, dp):

  if sm == 0:
    return 1
  
  if current_index == len(num):
    return 0
  
  if dp[current_index][sm] != -1:
    return dp[current_index][sm]

  if num[current_index] > sm:
    dp[current_index][sm] = canPartition(num, sm, current_index+1, dp)
  else:
    dp[current_index][sm] = canPartition(num, sm-num[current_index], current_index+1, dp) or canPartition(num, sm, current_index+1, dp)
  
  return dp[current_index][sm]
