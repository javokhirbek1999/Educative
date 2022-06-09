from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):

    node = Node(value)

    if lst.is_empty():
        lst.head_node = node
        return

    current = lst.head_node

    while current.next_element:
        current = current.next_element

    current.next_element = node
    return lst 
