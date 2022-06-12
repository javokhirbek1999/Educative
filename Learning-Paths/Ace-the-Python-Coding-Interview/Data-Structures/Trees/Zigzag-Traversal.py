class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  
  if not root:
    return result

  queue = [root]
  t = 0
  leftToRight = True
  while queue:
    temp = []
    max_len = len(queue)

    while max_len > 0:

      node = queue.pop(0)

      if leftToRight:
        temp.append(node.val)
      else:
        temp.insert(0, node.val)

      if node.left:
        queue.append(node.left)
        
      if node.right:
        queue.append(node.right)
      
      max_len -= 1
    leftToRight = True if not leftToRight else False
    
    result.append(temp)

  return result
