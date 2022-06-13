from binary_tree import *
from binary_tree_node import *


def print_right_boundry(root):

    if root:

        if root.right:
            print_right_boundry(root.right)
            print(root.data, end=", ")
        
        elif root.left:
            print_right_boundry(root.left)
            print(root.data, end=", ")

def print_left_boundry(root):

    if root:

        if root.left:
            print(root.data, end=", ")
            print_left_boundry(root.left)
        elif root.right:
            print(root.data, end=", ")
            print_left_boundry(root.right)

def print_leaves(root):

    if root:
        print_leaves(root.left)

        if not root.left and not root.right:
            print(root.data, end=", ")
        
        print_leaves(root.right)

def display_tree_perimeter(root):
    
    if root:
        print(root.data, end=", ")
        print_left_boundry(root.left)

        print_leaves(root)

        print_right_boundry(root.right)
    print()

    # print(result, end="")
