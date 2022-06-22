def binary_search(lst, target):
    low = 0
    high = len(lst)-1

    while low <= high:

        mid = low + (high - low) // 2

        if lst[mid] == target:
            return True
        
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    for num in lst:
        index = binary_search(lst, n-num)
        if index:
            return [num, n-num]
    
    return None
