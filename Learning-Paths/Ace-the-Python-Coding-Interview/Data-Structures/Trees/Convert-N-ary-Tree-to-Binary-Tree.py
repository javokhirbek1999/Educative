from binary_tree import *
from binary_tree_node import *
from n_ary_tree_node import *
from n_ary_tree import *

def convert_n_ary_to_binary_rec(node, is_left):

	if not node:
		return
	
	binary_tree_node = BinaryTreeNode(node.data)

	last_node = binary_tree_node


	for child in node.children:

		if not child:
			continue

		if is_left:
			last_node.left = convert_n_ary_to_binary_rec(child, not is_left)
			last_node = last_node.left
		else:
			last_node.right = convert_n_ary_to_binary_rec(child, not is_left)
			last_node = last_node.right
	
	return binary_tree_node



def convert_n_ary_to_binary(node):
	
	is_left_skewed = True

	return convert_n_ary_to_binary_rec(node, is_left_skewed)

def convert_binary_to_n_ary_rec(node, num_node, is_left):

	if not node:
		return 
	
	nAryNode = NaryTreeNode(node.data, num_node)

	ind = 0

	temp = node


	if is_left == 1:
		while temp.left:
			child = convert_binary_to_n_ary_rec(temp.left, num_node, 0)
			nAryNode.children[ind] = child
			ind += 1
			temp = temp.left
	else:
		while temp.right:
			child = convert_binary_to_n_ary_rec(temp.right, num_node, 1)
			nAryNode.children[ind] = child
			ind += 1
			temp = temp.right
	
	return nAryNode

def convert_binary_to_n_ary(node, num_node):
	
	return convert_binary_to_n_ary_rec(node, num_node, 1)
