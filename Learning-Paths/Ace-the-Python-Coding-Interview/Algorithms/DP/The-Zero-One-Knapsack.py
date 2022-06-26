"""
n = # of items
c = # capacity

Time: O(n * c)
Space: O(n)

"""
def optimized_rec(profits, profits_length, weights, capacity, current_index, dp):

    if current_index < 0 or current_index >= profits_length or capacity <= 0:
        return 0
    
    if dp[current_index][capacity] != 0:
        return dp[current_index][capacity]
    
    profit1 = 0
    if weights[current_index] <= capacity:
        profit1 = profits[current_index] + optimized_rec(profits, profits_length, weights, capacity-weights[current_index], current_index+1, dp)
    
    profit2 = optimized_rec(profits, profits_length, weights, capacity, current_index+1, dp)

    dp[current_index][capacity] = max(profit1, profit2)

    return dp[current_index][capacity]


def optimized(profits, profits_length, weights, capacity):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(profits_length + 1)]
    return optimized_rec(profits, profits_length, weights, capacity, 0, dp)
