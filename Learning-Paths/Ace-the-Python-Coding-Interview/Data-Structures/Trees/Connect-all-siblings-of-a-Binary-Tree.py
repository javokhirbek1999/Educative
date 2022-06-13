from binary_tree import *
from binary_tree_node import *

# Function to populate same level pointers
def populate_next_node_pointers(node):
    # TODO: Write - Your - Code
    if not node:
        return None
    
    queue = [node]
    levels = []
    while queue:
        node = queue.pop(0)
        levels.append(node)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)
    
    for i in range(len(levels)-1):
        levels[i].next = levels[i+1]
