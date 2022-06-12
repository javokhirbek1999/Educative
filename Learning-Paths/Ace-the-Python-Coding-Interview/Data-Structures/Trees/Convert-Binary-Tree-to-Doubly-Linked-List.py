from binary_tree import *
from binary_tree_node import *

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None
    
# class DLL:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def build(self, arr):

def rec(root):
    global head
    global tail


    if not root:
        return 
    
    rec(root.left)

    node = root

    if not head:
        head = node
    else:
        tail.right = node
        node.left = tail
    tail = node

    rec(root.right)

    return head

def convert_to_linked_list(root):
    # TODO: Write - Your - Code
    global head
    global tail

    if not root:
        return None
    
    head = None
    tail = None

    rec(root)

    head.left = None
    tail.right = None

    return head


