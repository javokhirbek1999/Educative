# Importing required functions
from binary_tree import *
from binary_tree_node import *

def are_identical(root1, root2):
    # TODO: Write - Your - Code

    return check(root1, root2)

def check(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 and r2 or r1 and not r2:
        return False
    
    if r1.data != r2.data:
        return False
    
    return check(r1.left, r2.left) and check(r1.right, r2.right)
