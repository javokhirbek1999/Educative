"""
Time: O(n)
Space: O(1)

"""
def find_minimum(arr):
    
    mn = arr[0]

    for i in arr:
        mn = min(mn, i)
    
    return mn
