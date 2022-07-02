"""
Time: O(log n)
Space: O(1)
"""
def find_closest(lst, target):
    """
    Finds the closest number to the target in the list
    :param lst: Sorted list of integers
    :param target: Left sided index of the list
    :return: Closest element from the list to the target
    """

    low = 0
    high = len(lst)-1
    
    while low <= high:

        mid = low + (high - low) // 2

        if lst[mid] == target:
            break
        
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return lst[low-1]
