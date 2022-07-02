def minimum_steps(lst):
    """
    Function which calculates the minimum steps to collect coins from the list
    :param lst: List of coins stack
    :return: Returns minimum steps to collect coins from the list, otherwise 0
    """
    
    mx, ind = lst[0], 0

    for index in range(len(lst)):

        if lst[index] > mx:
            mx = lst[index]
            ind = index
    
    return ind + abs((len(lst)-ind)-ind)
