# Importing required functions
from collections import deque
from binary_tree import *
from binary_tree_node import *

# Function that prints the in-order traversal of the binary tree
def inorder_iterative(root):

  if not root:
    print(None)
    return 
  
  current = root
  stack = []

  while True:

    if current:

      stack.append(current)

      current = current.left
    
    elif stack:

      current = stack.pop()

      print(current.data, end=", ")
      
      current = current.right
    else:
      break
