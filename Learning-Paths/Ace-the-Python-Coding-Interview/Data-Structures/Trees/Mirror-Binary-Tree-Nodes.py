from binary_tree import *
from binary_tree_node import *

def mirror_binary_tree(root):
    # TODO: Write - Your - Code
    
    if not root:
        return root
    
    queue = [root]

    while queue:

        node = queue.pop(0)

        node.left, node.right = node.right, node.left


        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
    
    return root
