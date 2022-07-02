def inversion_count(lst):
    """
    Function to find Inversion Count
    :param lst: List of integers
    :return: The inversion count of the list
    """

    n = len(lst)

    inversions = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                inversions += 1
    
    return inversions
