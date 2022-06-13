import math
from binary_tree import *
from binary_tree_node import *


DEFAULT = -math.inf

def serialize_rec(root, stream):

  if not root:
    stream.append(DEFAULT)
    return

  stream.append(root.data)

  serialize_rec(root.left, stream)
  serialize_rec(root.right, stream)


# Function to serialize tree into list of integer.
def serialize(root):
  stream = []

  serialize_rec(root, stream)

  return stream

# Function to deserialize integer list into a binary tree.
def deserialize(stream):

  if not stream:
    return

  val = stream.pop(0)

  if val == DEFAULT:
    return None
  
  node = BinaryTreeNode(val)

  node.left = deserialize(stream)
  node.right = deserialize(stream)

  return node
