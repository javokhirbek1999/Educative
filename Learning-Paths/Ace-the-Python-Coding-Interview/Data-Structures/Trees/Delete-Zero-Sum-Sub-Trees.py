from binary_tree import *
from binary_tree_node import *

def delete_zero_sum_subtree(tree):

    if not tree or not tree.root:
        return 
    
    sumTree = helper(tree.root)

    if sumTree <= 0:
        tree.root = None
    

def helper(root):

    if not root:
        return 0
    
    sumLeft = helper(root.left)
    sumRight = helper(root.right)

    if sumLeft == 0:
        root.left = None
    
    if sumRight == 0:
        root.right = None

    return root.data + sumLeft + sumRight

    
