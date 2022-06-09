from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):

    current = lst.get_head()

    visited = {}

    if current:
        visited[current.data] = 1
    else:
        return lst

    while current.next_element:
        if current.next_element.data in visited:
            current.next_element = current.next_element.next_element
        else:
            visited[current.next_element.data] = 1
            current = current.next_element
    
    return lst
