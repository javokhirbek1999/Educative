"""
Time: O(n * m)
Space: O(n * m)
"""
def can_partition(num):

  total = sum(num)

  if total % 2 == 1:
    return False
    
  target = total//2

  dp = [[-1 for _ in range(target+1)] for _ in range(len(num)+1)]

  return True if canPartition(num, 0, target, dp) == 1 else False

def canPartition(nums, index, target, dp):

  if target == 0:
    return 1

  if index == len(nums):
    return 0

  if dp[index][target] != -1:
    return dp[index][target]

  if nums[index] > target:
    dp[index][target] = canPartition(nums, index+1, target, dp) 
  else:
    dp[index][target] = canPartition(nums, index+1, target-nums[index], dp) or canPartition(nums, index+1, target, dp)
  
  return dp[index][target]
