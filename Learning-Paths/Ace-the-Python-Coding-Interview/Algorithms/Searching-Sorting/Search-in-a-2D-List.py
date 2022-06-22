"""
Approach #1:

Intuition: Perform Binary Search for both rows and columns

n = size of rows
m = size of columns

Time: O(log n + log m)
Space: O(1)
"""

def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    rows = len(lst)

    if not lst:
        return False
    
    cols = len(lst[0])

    if cols == 0:
        return False
    
    i = 0
    j = rows - 1

    if rows > 1:
        while i <= j:
            mid = i + (j - i) // 2

            if number == lst[mid][cols-1]:
                return True
            
            if number > lst[mid][cols-1]:
                i = mid + 1
            else:
                j = mid - 1
        
        if number > lst[mid][cols-1]:
            rows = mid +1
        else:
            rows = mid
    else:
        rows = 0
    
    if rows >= len(lst):
        return False
    
    i = 0
    j = cols - 1

    while i <= j:
        mid = i + (j - i) // 2

        if lst[rows][mid] == number:
            return True
        
        if number > lst[rows][mid]:
            i = mid + 1
        else:
            j = mid - 1
    
    return False
  
  

"""
Approach #2

Intuition: Perform Binary Search for each sub-array

Time: O(n log n)
Space: O(1)

"""

def find_in(lst, number):
    """
    A function to find a number in a 2D list
    :param lst: A 2D list of integers
    :param number: A number to be searched in the 2D list
    :return: True if the number is found, otherwise False
    """

    for sub in lst:
        found = binary_search(sub, number)
        if found:
            return True
    
    return False

    

def binary_search(arr, target):

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high-low) // 2

        current = arr[mid]

        if current == target:
            return True
        
        elif current < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False
