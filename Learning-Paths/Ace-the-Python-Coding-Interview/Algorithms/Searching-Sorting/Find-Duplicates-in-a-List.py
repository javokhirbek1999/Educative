"""
Appraoch #1: using dictionary/map

Time: O(n)
Space: O(n)
"""

from collections import defaultdict
def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []  # A list to store duplicates

    d = defaultdict(int)

    for i in lst:
        d[i] += 1
    
    for i in d.keys():
        if d[i] > 1:
            result.append(i)
    
    return result


  
"""
Approach #2: Sorting
  
Algorithm: Merge Sort
  
Time: O(n log n )
Space: O(n)
"""

def find_duplicates(lst):
    """
    Function to find duplicates in a given lst
    :param lst: A list of integers
    :return: A list of duplicate integers with no repetition
    """

    result = []

    merge_sort(lst)

    print(lst)

    prev = None
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] and lst[i] != prev:
            prev = lst[i]
            result.append(lst[i])
    
    return result


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
