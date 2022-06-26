"""
DP Approach: Top Down

Time: O(n)
Space: O(n)
"""
def count_ways_rec(n, dp):

    d = {0:1, 1:1, 2:2, 3:4}

    if n in d:
        return d[n]
    
    
    if n-1 not in dp:
        dp[n-1] = count_ways_rec(n-1, dp)
    
    if n-2 not in dp:
        dp[n-2] = count_ways_rec(n-2, dp)
    
    if n-3 not in dp:
        dp[n-3] = count_ways_rec(n-3, dp)
    
    return dp[n-1] + dp[n-2] + dp[n-3]

  
"""
DP Aprroach: Bottom Up

Time: O(n)
Space: O(1)
"""
def count_ways(n):
    """
    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """

    dp = [1,1,2]

    if 0 <= n < 3:
        return dp[n]

    for _ in range(3, n):
        current = dp[0] + dp[1] + dp[2]
        dp[0] = dp[1]
        dp[1] = dp[2]
        dp[2] = current
    
    return sum(dp)
   
    


