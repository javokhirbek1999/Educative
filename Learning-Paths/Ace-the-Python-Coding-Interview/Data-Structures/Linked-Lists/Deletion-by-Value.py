from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Search for element => list.search()
# Node class  { int data ; Node next_element;}


def delete(lst, value):
    

    current = lst.get_head()

    if not current:
        return False

    if current.data == value:
        current = current.next_element
        return True

    while current.next_element:
        if current.next_element.data == value:
            current.next_element = current.next_element.next_element
            return True
        else:
            current = current.next_element
    
    return False
