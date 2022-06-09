from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Searches a value in the given list.


def search(lst, value):
    
    if not lst.head_node:
        return False
    else:
        current = lst.head_node

        if current.data == value:
            return True
        
        while current:

            if current.data == value:
                return True

            current = current.next_element
        
        return False
