from binary_tree import *
from binary_tree_node import *


class InorderIterator:
    def __init__(self, root):
        # Initializing the stack variable
        self.stk = []

        # Assuming that when iterator is initialized
        # it is always at the first element of tree in its in-order
        self.populate_iterator(root)

    def populate_iterator(self, root):
        while root:
            self.stk.append(root)
            root = root.left

    # This function checks if there is a node next in line inside the iterator
    def hasNext(self):
        if not self.stk:
            return False
        else:
            return True

    # getNext returns null if there are no more elements in tree
    def getNext(self):
        if not self.stk:
            return None

        r_val = self.stk[-1]
        del self.stk[-1]
        temp = r_val.right
        self.populate_iterator(temp)

        return r_val

# Iterator helper function (Don't modify it)
# This function returns the in-order list of nodes using the hasNext() and
# getNext() methods

def inorder_using_iterator(root):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        if iter.hasNext():
            result += str(ptr.data) + ", "
        else:
            result += str(ptr.data)
    if result == "":
        result = "None"
    return result
