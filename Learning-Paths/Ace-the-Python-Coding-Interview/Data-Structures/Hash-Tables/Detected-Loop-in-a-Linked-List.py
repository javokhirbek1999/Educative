"""
Problem Statement#
  By definition, a loop is formed when a node in your linked list points to a previously traversed node.

You must implement the detect_loop() function which will take a linked list as input and deduce whether or not a loop is present.

You have already seen this challenge previously in chapter 3 of this course. Here you would use HashTables for a more efficient solution.

Input#
  A singly linked list.

Output#
  Returns True if the given linked list contains a loop. Otherwise, it returns False

Sample Input#
  LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.

Sample Output#
  True
"""


"""
Using a Hash-Table 

Time: O(n)
Space: O(n)
"""

def detect_loop(lst):
    
    d = {}

    current = lst.head_node

    while current:
        if current in d:
            return True
        d[current] = 1
        current = current.next_element

    return False
  
""" 
Using Tow Pointers

Time: O(n)
Space: O(1)

"""

def detect_loop(lst):

    current = lst.head_node

    slow, fast = current, current.next_element

    while fast and fast.next_element:
        fast = fast.next_element.next_element
        slow = slow.next_element
        
        if fast is slow:
            return True

    return False
