from collections import deque
from binary_tree import *
from binary_tree_node import *

def findMin(root):

    if not root:
        return None

    while root.left:
        root = root.left

    return root

def parent_successor_helper(node):

    while node.parent:
        if node.parent.left == node:
            return node.parent
        node = node.parent
    
    return None

def in_order_successor_helper(root):

    if not root:
        return None
    
    if root.right:
        return findMin(root.right)
    
    return parent_successor_helper(root)

def find_inorder_successor(root, predecessor_data):
    
    while root:
    
        if root.data < predecessor_data:
            root = root.right
        elif root.data > predecessor_data:
            root = root.left
        else:
            return in_order_successor_helper(root)
    
        if not root:
            return BinaryTreeNode(-1)
    
    return None



