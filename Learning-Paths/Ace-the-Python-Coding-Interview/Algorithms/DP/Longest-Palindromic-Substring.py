def rec(s, start, end, dp):

    if start > end:
        return 0
    
    if start == end:
        return 1

    pos = "{},{}".format(start,end)

    if pos in dp:
        return dp[pos]


    pos = "{},{}".format(start+1,end-1)

    if s[start] == s[end]:
        dp[pos] = 2 + rec(s, start+1, end-1, dp)
    
    pos1 = "{},{}".format(start+1,end)
    pos2 = "{},{}".format(start,end-1)


    if pos1 not in dp:
        dp[pos1] = rec(s, start+1, end, dp)
    
    if pos2 not in dp:
        dp[pos2] = rec(s, start, end-1, dp)

    print(max(dp[pos1], dp[pos2]))
    return max(dp[pos1], dp[pos2])


def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of shortest common superstring
    """

    dp = {}

    return rec(s, 0, len(s)-1, dp)
