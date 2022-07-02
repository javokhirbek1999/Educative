def find_floor(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the floor of an integer x if exists, otherwise -1
    """
    while low <= high:
        mid = low + (high - low)//2

        current = lst[mid]

        if current == x:
            break
        
        if current < x:
            low = mid + 1
        else:
            high = mid - 1
    
    if low <= 0:
        return -1
    return lst[low-1]

def find_ceiling(lst, low, high, x):
    """
    Modified binary search function to find the floor of given number x
    :param lst: List of integers
    :param low: Starting index of the list
    :param high: Ending index of the list
    :return: Returns the ceiling of an integer x if exists, otherwise -1
    """

    while low <= high:

        mid = low + (high - low) // 2


        current = lst[mid]

        if current == x:
            break
        
        if current < x:
            low = mid + 1
        else:
            high = mid - 1
    
    if low >= len(lst)-1:
        return -1
    
    return lst[low]
    

def find_floor_ceiling(lst, x):
    # DO NOT MODIFY THIS FUNCTION #

    """
    Calls the find_floor and find_ceiling functions and returns their results
    :param lst: List of integers
    :param x: An integer
    :return: Returns the floor of an integer x, otherwise -1
    """
    # lst.append(x)
    # lst.sort()
    return find_floor(lst, 0, len(lst) - 1, x), find_ceiling(lst, 0, len(lst) - 1, x)
