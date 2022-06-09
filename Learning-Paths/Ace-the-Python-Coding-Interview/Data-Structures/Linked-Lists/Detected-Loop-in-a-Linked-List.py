from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def detect_loop(lst):
    
    slow, fast = lst.get_head(), lst.get_head()

    while fast:

        slow = slow.next_element

        fast = fast.next_element.next_element

        if fast is slow:
            return True
    return False
