"""
Problem Statement#
  In this problem, you have to implement the findSum(lst,k) function which will take a number k as input and return two numbers that add up to k.

You have already seen this challenge previously in chapter 2 of this course. Here you would use HashTables for a more efficient solution.

Input#
  A list and a number k

Output#
  A list with two integers a and b that add up to k

Sample Input#
  lst = [1,21,3,14,5,60,7,6]
  k = 81
  
Sample Output#
  lst = [21,60]
  
For example, in this illustration, we are given 81 as the number k and when we traverse the whole list we find that 21 and 60 are the integers that add up to 81.

"""

def findSum(lst, k):
    
    d = {k-i:i for i in lst}

    for i in lst:
        if i in d and i != d[i]:
            return [d[i], i]
    
    return None
