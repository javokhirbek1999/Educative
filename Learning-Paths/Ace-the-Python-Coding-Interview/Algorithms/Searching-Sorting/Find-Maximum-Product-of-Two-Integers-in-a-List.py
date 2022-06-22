# Decimal library to assign infinite numbers
import math
from decimal import Decimal


def find_max_prod(lst):
    """
    Finds the pair having maximum product in a given list
    :param lst: A list of integers
    :return: A pair of integer
    """

    first, second = -math.inf, -math.inf 

    for i in lst:
        if i > first:
            second = first
            first = i
        elif i > second and i != first:
            second = i
    
    if second == 0 and first > 0:
        second = first
    elif first == 0 and second > 0:
        first = second

    return first, second
