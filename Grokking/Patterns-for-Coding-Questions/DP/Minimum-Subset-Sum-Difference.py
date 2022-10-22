"""
Time: O(n * m)
Space: O(n * m)

"""
def can_partition(num):

  dp = {}

  return partition(num, 0, 0, 0, dp)

def partition(num, index, sum1, sum2, dp):

  if index == len(num):
    return abs(sum1-sum2)

  key = (index, sum1, sum2)

  if key in dp:
    return dp[key]
  
  sub1 = partition(num, index+1, sum1+num[index], sum2, dp)
  sub2 = partition(num, index+1, sum1, sum2+num[index], dp)

  dp[key] = min(sub1, sub2)
  
  return dp[key]
