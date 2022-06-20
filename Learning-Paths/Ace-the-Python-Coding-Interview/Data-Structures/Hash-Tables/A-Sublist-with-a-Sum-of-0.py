"""

Problem Statement#
You must implement the find_sub_zero(my_list) function which will take in a list of positive and negative integers. It will tell us if there exists a sublist in which the sum of all elements is zero. The term sublist implies that the elements whose sum is 0 must occur consecutively.

A list with these contents would return True:
[6, 4, -7, 3, 12, 9]

Whereas this would return False as the elements which sum up to be 0 do not appear together:
[-7, 4, 6, 3, 12, 9]

Input#
A list containing positive and negative integers.

Output#
Returns True if there exists a sublist with its sum equal to 0. Otherwise, the function returns False.

Sample Input#
  my_list = [6, 4, -7, 3, 12, 9]
Sample Output#
  True

"""
def find_sub_zero(my_list):

    for i in range(len(my_list)):
        current_sum = 0
        for j in range(i,len(my_list)):
            
            current_sum += my_list[j]

            if current_sum == 0:
                return True
    
    return False
