from binary_tree import *
from binary_tree_node import *

def find_min(root):

    while root.left:
        root = root.left
    
    return root

def find_inorder_successor(root, node_value):
    # TODO: Write - Your - Code
    if not root:
        return None
    
    successor = None

    while root:

        if root.data < node_value:
            root = root.right
        elif root.data > node_value:

            successor = root

            root = root.left
        else:
            if root.right:
                successor = find_min(root.right)
            break
    
    if not root:
        return BinaryTreeNode(-1)
    return successor

