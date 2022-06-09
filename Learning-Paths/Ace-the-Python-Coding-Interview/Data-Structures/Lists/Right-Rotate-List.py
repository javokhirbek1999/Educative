"""

Time: O(n)
Space: O(n)

"""
def right_rotate(lst, k):
    n = len(lst)

    if n == 0:
        k = 0
    else:
        k = k % n
    
    result = []

    for i in range(n-k, n):
        result.append(lst[i])
    
    for i in range(0, n-k):
        result.append(lst[i])
    
    return result
