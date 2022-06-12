from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  if not root:
    return None
  
  queue = [root]

  while queue:
    prevNode = None
    max_len = len(queue)

    for _ in range(max_len):

      currentNode = queue.pop(0)

      if prevNode is not None:
        prevNode.next = currentNode
      
      prevNode = currentNode


      if currentNode.left:
        queue.append(currentNode.left)
      
      if currentNode.right:
        queue.append(currentNode.right)
    
