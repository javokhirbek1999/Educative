"""
Sorting with merge sort

Time: O(n log n)
Space: O(n)
"""

def sort_binary_list(lst):
    """
    A function to sort binary list
    :param lst: A list containing binary numbers
    :return: A sorted binary list
    """

    merge_sort(lst)

    return lst
    
def merge_sort(lst):

    mid = len(lst)//2

    if mid <= 0:
        return lst

    left = lst[:mid]
    right = lst[mid:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        
        k += 1
    
    
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
    
