from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  if not root:
    return None

  queue = [root]
  levels = []

  while queue:
    temp = []
    max_len = len(queue)

    while max_len > 0:

      node = queue.pop(0)

      temp.append(node.val)

      if node.left:
        queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
      
      max_len -= 1
    levels.append(temp)
    
  result = "\n"  
  for i in range(len(levels)-1, -1, -1):
    result += str(levels[i]) + "\n"
  

  # TODO: Write your code here
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
