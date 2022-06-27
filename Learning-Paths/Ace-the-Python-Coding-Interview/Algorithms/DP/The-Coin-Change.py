"""
Top-down:
Time: O(array_length * amount)
"""
def rec(denoms, denoms_length, amount, dp):

    if amount == 0:
        return 1
    
    if amount < 0 or denoms_length == 0:
        return 0
    
    if dp[denoms_length-1][amount] != 0:
        return dp[denoms_length-1][amount]
    
    dp[denoms_length-1][amount] = rec(denoms, denoms_length-1, amount, dp) + rec(denoms, denoms_length, amount-denoms[denoms_length-1], dp)

    return dp[denoms_length-1][amount]
    
def count_change(denoms, denoms_length, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denoms: Values of the coins available
    :param denoms_length: Number of denoms
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    dp = [[0 for _ in range(amount + 1)] for _ in range(denoms_length)]

    return rec(denoms, denoms_length, amount, dp)
