"""
Time: O(n)
Space: O(1)
"""
def find_peak(lst):
    """
    Finds a peak element
    :param lst: List of integers
    :return: Returns a peak element in a given list
    """

    first_mx = lst[0]
    second_mx = lst[-1]

    i = len(lst)//2

    while i > 0:

        first_mx = max(first_mx, lst[i])
        second_mx = max(second_mx, lst[-(i)])

        i -= 1
    
    return first_mx


"""
Time: O(log n)
Space: O(log n)
"""

def search(lst, low, high):

    mid = low + (high - low)//2

    if (mid == len(lst)-1 or lst[mid+1] <= lst[mid]) and (mid == 0 or lst[mid-1] <= lst[mid]):
        return mid
    
    elif (lst[mid-1] > lst[mid]) and mid > 0:
        return search(lst, low, mid-1)
    
    else:
        return search(lst, mid+1, high)


def find_peak(lst):
    """
    Finds a peak element
    :param lst: List of integers
    :return: Returns a peak element in a given list
    """

    ind = search(lst, 0, len(lst)-1)
    return lst[ind]
