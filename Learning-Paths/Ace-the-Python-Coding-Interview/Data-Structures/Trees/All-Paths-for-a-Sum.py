class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def findPathsRec(currentNode, allPaths, currentPath, target):

  if not currentNode:
    return 
  
  currentPath.append(currentNode.val)

  if currentNode.val == target and not currentNode.left and not currentNode.right:
    allPaths.append(list(currentPath))
  else:
    findPathsRec(currentNode.left, allPaths, currentPath, target-currentNode.val)
    findPathsRec(currentNode.right, allPaths, currentPath, target-currentNode.val)

  currentPath.pop()

def find_paths(root, sum):
  allPaths = []
  # TODO: Write your code here
  findPathsRec(root, allPaths, [], sum)
  return allPaths
