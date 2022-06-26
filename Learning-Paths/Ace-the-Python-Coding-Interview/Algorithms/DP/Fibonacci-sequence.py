"""
Top Down -> Memoization: 
  Disadvantage: Throws stack overflow exception for exteremely large inputs -> Because, all uniqueue recursive calls must be put on call stack 

Bottom Up -> Tabulation:
  Works pretty well for large inputs
"""
def topDown(n: int, dp={}) -> int:

    if n <= 1:
        return n
    if n-1 not in dp:
        dp[n-1] = topDown(n-1, dp)
    
    if n-2 not in dp:
        dp[n-2] = topDown(n-2, dp)
    
    return dp[n-1] + dp[n-2]


def bottomUp(n: int) -> int:

    dp = [0,1]

    for _ in range(2, n):
        dp[0] = dp[1]
        dp[1] = dp[0]+dp[1]
    

    return dp[-1]
