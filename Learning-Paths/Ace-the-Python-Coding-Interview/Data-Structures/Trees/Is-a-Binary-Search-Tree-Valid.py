from binary_tree import *
from binary_tree_node import *

import math

def is_bst(root):
    return validate(-math.inf, root, math.inf)

def validate(leftVal, root, rightVal):
    if not root:
        return True
    
    if not (leftVal < root.data < rightVal):
        return False
    
    return validate(leftVal, root.left, root.data) and validate(root.data, root.right, rightVal)
