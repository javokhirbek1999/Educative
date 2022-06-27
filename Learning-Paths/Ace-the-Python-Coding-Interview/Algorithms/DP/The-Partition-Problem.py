"""
Top-down: Memoization
Time: O(n)
Space: O(n)
"""
def partition(set, sm, currentIndex, dp):

    if sm == 0:
        return True

    if len(set) == 0 or currentIndex >= len(set):
        return False
    
    if currentIndex in dp:
        return dp[currentIndex]
    
    if set[currentIndex] <= sm:
        dp[currentIndex] = partition(set, sm-set[currentIndex], currentIndex+1, dp)
    
    dp[currentIndex+1] = partition(set, sm, currentIndex+1, dp)

    return dp[currentIndex]

def can_partition(set):
    """
    Checks if two sub-lists has equal sum or not
    :param set: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """

    sm = 0

    for i in set:
        sm += i
    
    if sm % 2 != 0:
        return False
    dp = {}
    return partition(set, sm, 0, dp)
