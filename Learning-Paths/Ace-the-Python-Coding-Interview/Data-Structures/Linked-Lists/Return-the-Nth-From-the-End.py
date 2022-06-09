from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Function to find the nth node from end of Linked List


def find_nth(lst, n):
    
    if (lst.is_empty()):
        return -1

    # Find Length of list
    length = lst.length() - 1

    # Find the Node which is at (len - n + 1) position from start
    current_node = lst.get_head()

    position = length - n + 1

    if position < 0 or position > length:
        return -1

    count = 0

    while count is not position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1


