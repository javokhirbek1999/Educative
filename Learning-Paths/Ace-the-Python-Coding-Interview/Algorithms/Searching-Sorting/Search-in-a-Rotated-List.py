def pivoted_binary_search(lst, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """

    ind = 0

    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            ind = i
            break
    
    left = lst[ind:]
    right = lst[:ind]

    print(left, right)

    l = binary_search(left, key)
    r = binary_search(right, key)

    if l > -1:
        return (len(left)-1)+l
    else:
        return r

def binary_search(lst, target):

    low = 0
    high = len(lst)-1

    while low <= high:
        
        mid = low + (high - low)//2

        if lst[mid] == target:
            return mid
        
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
