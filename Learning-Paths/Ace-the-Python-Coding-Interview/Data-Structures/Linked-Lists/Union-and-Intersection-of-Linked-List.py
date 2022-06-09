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

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    if list1.is_empty():
        return list2
    
    if list2.is_empty():
        return list1
    
    start = list1.get_head()

    while start.next_element:
        start = start.next_element
    
    start.next_element = list2.get_head()
    list1.remove_duplicates()

    return list1


# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here
    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value) is not None:
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    result.remove_duplicates()
    return result
