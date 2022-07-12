"""
Top Down (Memoization)

Time: O(n)
Space: O(n)
"""
def scoring_options(n):
  dp = {}
  return dp_top_down(n, dp)

def dp_top_down(n, dp):

  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  elif n == 2:
    return 2
  
  if n-1 not in dp:
    dp[n-1] = dp_top_down(n-1, dp)
  
  if n-2 not in dp:
    dp[n-2] = dp_top_down(n-2, dp)
  
  if n-4 not in dp:
    dp[n-4] = dp_top_down(n-4, dp)
  
  return dp[n-1] + dp[n-2] + dp[n-4]


"""
Bottom up
Time: O(n)
Space: O(n)
"""

# Scoring options are 1, 2, and 4
def scoring_options(n):
  
  dp = [1] * (n+1)


  sum1 = sum2 = sum3 = 0

  for current_index in range(1, n+1):

    sum1 = 0 if current_index-1 < 0 else dp[current_index-1]
    sum2 = 0 if current_index-2 < 0 else dp[current_index-2]
    sum3 = 0 if current_index-4 < 0 else dp[current_index-4]

    dp[current_index] = sum1+sum2+sum3
  
  return dp[n]
