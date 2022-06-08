"""
Time: O(n)
Space: O(n)
"""

def find_product(lst):
    
    left = 1

    res = []

    for i in range(len(lst)):
        res.append(left)
        left = left * lst[i]
    
    right = 1

    for i in range(len(res)-1, -1, -1):
        res[i] = res[i] * right
        right = right * lst[i]
    
    return res
