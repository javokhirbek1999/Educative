"""
Bottom Up
"""
def can_partition(num):

    total_sum = sum(num)

    dp = [[False for _ in range((total_sum//2)+1)] for _ in range(len(num))]

    for i in range(len(num)):
        dp[i][0] = True
    
    for i in range((total_sum//2)+1):
        dp[0][i] = num[0] == i

    
    for i in range(1, len(num)):
        for j in range(1, (total_sum//2)+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    
    sum1 = 0

    for i in range(total_sum//2, -1, -1):
        if dp[len(num)-1][i]:
            sum1 = i
            break
    
    sum2 = len(num)-sum1

    return abs(sum1-sum2)


"""
Top Down
"""
def topDown(num):

    dp = {}

    return canPartitionTopDown(num, 0, 0, 0, dp)

def canPartitionTopDown(num, current_index, sum1, sum2, dp):

    if current_index == len(num):
        return abs(sum1-sum2)

    if sum1+num[current_index] not in dp:
        dp[sum1+num[current_index]] = canPartitionTopDown(num, current_index+1, sum1+num[current_index], sum2, dp)
    if sum2+num[current_index] not in dp:
        dp[sum2+num[current_index]] = canPartitionTopDown(num, current_index+1, sum1, sum2+num[current_index], dp)
    
    return min(dp[sum1+num[current_index]], dp[sum2+num[current_index]])
