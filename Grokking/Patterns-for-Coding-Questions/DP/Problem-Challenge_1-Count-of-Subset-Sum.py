"""
Time: O(n * m)
Space: O(n * m)
"""
def count_subsets(num, sum):
  
  dp = {}

  return count(num, 0, sum, dp)

def count(nums, index, target, dp):

  if index == len(nums):
    if target == 0:
      return 1
    return 0
  
  key = (index, target)

  if key in dp:
    return dp[key]

  if nums[index] > target:
    dp[key] = count(nums, index+1, target, dp)
  else:
    dp[key] = count(nums, index+1, target-nums[index], dp) + count(nums, index+1, target, dp)
  
  return dp[key]
