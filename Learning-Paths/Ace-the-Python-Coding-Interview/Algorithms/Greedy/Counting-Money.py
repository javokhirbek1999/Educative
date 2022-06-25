"""
Time: O(n^2) 
"""

def find_min_coins(v, coins_available):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :param coins_available: Coins available in the machine
    :return: A list of total coins
    """

    res = []

    i = len(coins_available)-1

    while v > 0 or i > 0:

        current = coins_available[i]
        
        if current > v:
            i -= 1
        else:
            res.append(current)
            v -= current
    
    if v == 0:
        return res
    return None
