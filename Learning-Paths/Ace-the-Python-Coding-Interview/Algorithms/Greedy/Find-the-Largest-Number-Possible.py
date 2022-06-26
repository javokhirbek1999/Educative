"""
n = # of digits

Time: O(n)
Space: O(n)
"""

def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """

    key = [0]*number_of_digits

    i = 0
    while sum_of_digits > 10:

        if i < number_of_digits:
            key[i] = 9
            sum_of_digits -= 9
        else:
            return [-1]
        i += 1

    key[i] = sum_of_digits

    return key
