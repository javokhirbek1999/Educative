"""
n = size of array
k = size of sub-array

Time: O(n(k log k))
Space: O(n)
"""

from collections import defaultdict

def anagrams(lst):
    """
    Function to find anagram pairs
    :param lst: A lst of strings
    :return: Group of anagrams
    """
    
    d = defaultdict(list)

    for word in lst:
        
        temp = "".join(sorted(word))

        d[temp].append(word)
    
    return [i for i in d.values()]
