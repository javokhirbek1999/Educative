from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    
    current = lst.get_head()

    if not current:
        return 0
    
    c = 0

    while current:
        c += 1
        current = current.next_element
    
    return c
