"""
Problem Statement#
  Implement a function, findFirstUnique(lst) that returns the first unique integer in the list. Unique means the number does not repeat and appears only once in the whole list.

You have already seen this challenge previously in chapter 2 of this course. Here you would use dict or set for a more efficient solution.

Input#
  A list of integers

Output#
  The first unique element in the list

Sample Input#
  [9,2,3,2,6,6]

Sample Output#
  9
  
"""
def findFirstUnique(lst):
    
    d = {}
    t = {lst[i]:i for i in range(len(lst))}

    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    mn = len(lst)
    val = 0 
    for i in d.keys():
        if d[i] == 1:
            if t[i] < mn:
                mn = t[i]
                val = i
                
    return val

  
 """ Using OrderDict() """

from collections import OrderedDict

def findFirstUnique(lst):

    d = OrderedDict.fromkeys(lst, 0)

    for i in lst:
        d[i] += 1
    
    for elem in d.keys():
        if d.get(elem) == 1:
            return elem
    
    return -1
  
