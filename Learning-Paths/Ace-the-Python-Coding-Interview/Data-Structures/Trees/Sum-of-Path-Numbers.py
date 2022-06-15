"""
Solution #1
"""
def solve(currentNode, allPaths, currentPath):

  if not currentNode:
    return 
  
  currentPath.append(currentNode.val)

  if not currentNode.left and not currentNode.right:
    allPaths.append(int("".join([str(x) for x in currentPath])))

  solve(currentNode.left, allPaths, currentPath)
  solve(currentNode.right, allPaths, currentPath)

  currentPath.pop()

def find_sum_of_path_numbers(root):
  
  allPaths = []

  solve(root, allPaths, [])

  return sum(allPaths)
