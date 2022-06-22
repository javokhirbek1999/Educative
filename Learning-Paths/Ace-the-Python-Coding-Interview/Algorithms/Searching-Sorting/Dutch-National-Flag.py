"""
Appraoch #2: Three-way partitioning

Time: O(n)
Space: O(1)
"""

def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    i, mid, j = 0, 0, len(lst)-1

    while mid <= j:

        if lst[mid] == 0:
            lst[mid], lst[i] = lst[i], lst[mid]
            i += 1
            mid += 1
        elif lst[mid] == 2:
            lst[mid], lst[j] = lst[j], lst[mid]
            j -= 1
        else:
            mid +=1

    return lst

  
  


"""
Approach #2: Divide flag colors into seperate arrays and merge them in-order

Time: O(n)
Space: O(n)
"""

def dutch_national_flag(lst):
    """
    A function to solve Dutch National Flag Problem
    :param lst: A list of integers
    :return: A list of solved Dutch National Flag Problem
    """

    up, mid, down = [], [], []

    for i in lst:
        if i == 0:
            up.append(i)
        elif i == 1:
            mid.append(i)
        else:
            down.append(i)
    
    up.extend(mid)
    up.extend(down)

    return up
