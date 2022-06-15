class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_path_rec(currentNode, sequence, index):
  
  if not currentNode:
    return

  seqLen = len(sequence)

  if seqLen <= index or currentNode.val != sequence[index]:
    return False
  
  if not currentNode.left and not currentNode.right and index == seqLen-1:
    return True

  return find_path_rec(currentNode.left, sequence, index+1) or find_path_rec(currentNode.right, sequence, index+1) 

def find_path(root, sequence):
  
  return find_path_rec(root, sequence, 0)
  
